# Info
This repo aims to speed up the process of creating a private Shopify app using Python on Google App Engine. It leverages webapp2 for simple routing, and has functions to GET and POST to your Shopify store with JSON.

## Getting Started

### Hooking up your Shopify Store
1. Update the YOUR_SHOP portion of this line in app.yaml:

	SHOP_URL = "https://YOUR_SHOP.myshopify.com/admin/"

1. Log in to your store, and create a new Private App under Apps. Copy the key and password, and place them in app.yaml:

	SHOPIFY_API_KEY = 'xxxxxx'
	SHOPIFY_API_PASSWORD = 'xxxxxx'

### App Engine Instructions

1. Go to https://console.developers.google.com/ and register for an account. Create a new project, and copy its ID (this will looks something like my-project).
1. Open app.yaml, paste the ID to replace the XXXs under application.
1. Download and install https://cloud.google.com/appengine/downloads
1. Open the launcher you installed, and go to File > Add existing application
1. Click Run, then Browse. The app will pull up to 25 of your products from the store and display their titles.

### Main Functions
Two functions have been built to interact with your store: *shopPOST* and *shopGET*. These both take a Python Dict object, make the API call to a json endpoint, and return the result.

### Next
Once you have this basic example working, you can work on adding more routes to interact with different parts of the store, or build on the current one. See resources below for more info.

## Resources
- [Shopify API Reference](https://help.shopify.com/api/reference)
- [Web App 2](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/usingwebapp#hello-webapp2)
