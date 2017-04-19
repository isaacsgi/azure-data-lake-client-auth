## Python-Django ADLS / AAD-REST API Authentication Sample Application
This project enables a user to be authenticated via Azure Active Directory.  That Authentication is then used to access an 
Azure Data Lake Store (ADLS) where they've been defined by the ADLS owner as an authorized user.

The sample uses Python Django to create Azure REST API calls and take the user through a standard OAuth2 flow driven by 
Azure Active Directory (AAD).  Once successfully authenticated, AAD provides a secure Bearer token that is then used via the
ADLS REST API to enable that user's access to the ADLS instance.

