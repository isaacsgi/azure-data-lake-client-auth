## Building interactive authentication for Azure Data Lake with Azure AD

Many Business Intelligence and Analytics apps want to use data in Azure Data Lake Store,ADLS, due to the many features of ADLS.

The goal of this project is to demonstrate how to build applications for human user interaction (interactive user, not a service) with ADLS data and execute various Business Intelligence scenarios and use cases. We will initially create example code using C++ and connect to one popular analytics tool. Next, we will expand the example base to other code (node.js, etc) and other popular analytics tools. 

This will include: 

1. Authentication of Interactive User to ADLS/HDFS layer via Azure AD
   - ADLS presents an HDFS interface

2. Navigation of ADLS Folder structure
   - Browsing ADLS content

3. Modification of data contents
   - usual CRUD functions

4. Connection to Analytics tool
   - Visualization capabilities are critical to data insight and Business Intelligence use

ADLS enables you to store data of any size, shape, and speed, and do all types of processing and analytics across platforms and languages. It removes the complexities of ingesting and storing all of your data while making it faster to get up and running with batch, streaming, and interactive analytics. Due to the number of separate pieces required to make this work, it became clear that a project to show how to do it would be useful.

Here's a great reference book:

[Modern authentication with Azure Active Directory for Web applications
2016, by Bertocci, Vittorio.] (http://mslibrary/SearchCenter/Pages/LibrarySimple.aspx?k=Title%3A%22Modern%20authentication%20with%20Azure%20Active%20Directory%20for%20Web%20applications%22)

##Some items of interest:

[1.Setting up Active Directory and Data Lake Store (includes java and .net sample)](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-end-user-authenticate-using-active-directory )

[2. Getting started](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-portal)

[Getting started with Data Lake Storage using REST api](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-rest-api )

[Securing a web API with Azure AD](https://github.com/Azure-Samples/active-directory-node-webapi)

##Here is how to use Azure AD web app to authenticate with ADLS and then perform other operations on ADLS:
 - [.Net SDK](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-net-sdk)
 - [Java SDK](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-get-started-java-sdk)

[Securing data in ADLS](https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-secure-data)

[Use Curl](http://curl.haxx.se/)

[Here's where sample data is](https://github.com/MicrosoftBigData/usql/tree/master/Examples/Samples/Data/AmbulanceData)

[What is an Azure AD Tenant?](https://msdn.microsoft.com/en-us/library/azure/jj573650.aspx?#BKMK_WhatIsAnAzureAD)

[If you need to install Azure CLI](https://docs.microsoft.com/en-us/azure/xplat-cli-install)
