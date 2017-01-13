# Project for demonstrating how to build interactive authentication for Azure Data Lake

Many Business Intelligence and Analytics apps want to use data in Azure Data Lake Store,ADLS, due to the many features of ADLS.

The goal of this project is to demonstrate how to build applications for human user interaction (interactive user, not a service) with ADLS data and execute various Business Intelligence scenarios and use cases. We will initially create example code using C++ and connect to one popular analytics tool. Next, we will expand the example base to other code (node.js, etc) and other popular analytics tools. 

This will include: 
Authentication of Interactive User to ADLS/HDFS layer via Azure AD
ADLS presents an HDFS interface
Navigation of ADLS Folder structure and browse data
CRUD Access to data contents
Plug in visualization capabilities of choice to fulfill data analysis for Business Intelligence use

ADL enables you to store data of any size, shape, and speed, and do all types of processing and analytics across platforms and languages. It removes the complexities of ingesting and storing all of your data while making it faster to get up and running with batch, streaming, and interactive analytics. Due to the number of separate pieces required to make this work, it became clear that a project to show how to do it would be useful.

Here's a great reference book:

[Modern authentication with Azure Active Directory for Web applications
2016, by Bertocci, Vittorio.] (http://mslibrary/SearchCenter/Pages/LibrarySimple.aspx?k=Title%3A%22Modern%20authentication%20with%20Azure%20Active%20Directory%20for%20Web%20applications%22)

Some items of interest:


## Getting started with Data Lake Storage using REST api
https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-rest-api 

##Setting up Active Directory and Data Lake Store (includes java and .net sample)
https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-end-user-authenticate-using-active-directory 

##Securing a web API with Azure AD
https://github.com/Azure-Samples/active-directory-node-webapi
