from django.shortcuts import render, redirect, get_object_or_404
from xml.dom.minidom import parseString
import requests
from requests_oauthlib import OAuth2Session
from django.conf import settings
import logging
import sys, json

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from django.template import loader

# from .models import Question, Choice

def index(request):
	context = {'initialize':''}
	return render(request, 'adlsauth/index.html', context)

def step1(request):	
	# initialization
	constants = settings.CONSTANTS
	CLIENT_ID = constants['CLIENT_ID']
	STEP_1_TEMPLATE_NAME = constants['STEP_1_TEMPLATE_NAME']
	REDIRECT_URI = constants['REDIRECT_URI']
	AUTHORIZATION_BASE_URL = constants['AUTHORIZATION_BASE_URL']
	
	context = {'initialize':''}
	
	# GET as a result of initial invocation
	if request.method == 'GET':
		
		# initial invocation, just render
		return render(request, STEP_1_TEMPLATE_NAME, context)
		
	# OAUTH STEP 1 - POST as a result of clicking the LogIn submit button	
	elif request.method == 'POST':

		# create a 'requests' Oauth2Session
		azure_session = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)

		# do the outreach to https://login.windows.net/common/oauth2/authorize
		authorization_url, state = azure_session.authorization_url(AUTHORIZATION_BASE_URL)
		resp = requests.get(authorization_url)		
		
		# go to the login page of AAD & authenticate
		return redirect(resp.url)

def step2(request):

	# initialization
	constants = settings.CONSTANTS
	STEP_2_TEMPLATE_NAME = constants['STEP_2_TEMPLATE_NAME']
	STEP_3_TEMPLATE_NAME = constants['STEP_3_TEMPLATE_NAME']
	BASE_TOKEN_URL = constants['BASE_TOKEN_URL']
	REDIRECT_URI = constants['REDIRECT_URI']
	CLIENT_ID = constants['CLIENT_ID']
	CLIENT_KEY = constants['CLIENT_KEY']
	RESOURCE_URI = constants['RESOURCE_URI']
	
	context = {'initialize':''}
	azure_session = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
	
	if request.method == 'GET':
	
		# get the code returned by AAD and save it in session
		aad_code = request.GET.get('code','')
		request.session['aad_code'] = aad_code

		# display the code
		context['aad_code'] = aad_code
		
		return render(request, STEP_2_TEMPLATE_NAME, context)
		
	elif request.method == 'POST':
	
		# get code back from session
		aad_code = request.session['aad_code']

		# OAUTH STEP 2 - go fetch the token
		token_dict = azure_session.fetch_token(BASE_TOKEN_URL, code=aad_code, client_secret=CLIENT_KEY, resource=RESOURCE_URI)
		
		# pass the token to the next step on session
		request.session['token'] = token_dict

		# display the token
		context['token'] = token_dict
		
		return render(request, STEP_3_TEMPLATE_NAME, context)

def step3(request):

	# initialization
	constants = settings.CONSTANTS
	STEP_3_TEMPLATE_NAME = constants['STEP_3_TEMPLATE_NAME']
	STEP_4_TEMPLATE_NAME = constants['STEP_4_TEMPLATE_NAME']
	CLIENT_ID = constants['CLIENT_ID']
	REDIRECT_URI = constants['REDIRECT_URI']
	GET_SUBSCRIPTIONS_URL = constants['GET_SUBSCRIPTIONS_URL']
	MS_API_VERSION_HEADER = constants['MS_API_VERSION_HEADER']
	MS_API_VERSION_HEADER_VALUE = constants['MS_API_VERSION_HEADER_VALUE']
	MS_API_VERSION_DATA_LAKE_VALUE = constants['MS_API_VERSION_DATA_LAKE_VALUE']
	DATA_LAKE_OPERATION = constants['DATA_LAKE_OPERATION']
	DATA_LAKE_LIST_FOLDERS = constants['DATA_LAKE_LIST_FOLDERS']
	DATA_LAKE_URI = constants['DATA_LAKE_URI']

	context = {'initialize':''}
	
	if request.method == 'GET':
		return render(request, STEP_3_TEMPLATE_NAME, context)
		
	elif request.method == 'POST':

		# create a requests session with the token we got previously
		token = request.session['token']
		azure_session = OAuth2Session(CLIENT_ID, redirect_uri = REDIRECT_URI, token=token)
		
		# OAUTH STEP 3 - go get the subscriptions
		resp = azure_session.get(DATA_LAKE_URI, headers = {MS_API_VERSION_HEADER: MS_API_VERSION_DATA_LAKE_VALUE},params= {DATA_LAKE_OPERATION: DATA_LAKE_LIST_FOLDERS})
		
		print(">>Hello <<", end='\n', file=sys.stdout)
		print(resp.status_code, end='\n', file=sys.stdout)		
		print(resp.json(), end='\n', file=sys.stdout)
		context ['filestati'] = resp.json()

		return render(request, STEP_4_TEMPLATE_NAME, context)
		
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
