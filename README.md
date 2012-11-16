Python Package for AuthorityLabs Partner API
=============================

A wrapper around the Partner API calls. Allows post, priority post and get calls.

* Github: http://github.com/mtchavez/py_al_papi
* PyPi: http://pypi.python.org/pypi/al_papi
* [![endorse](http://api.coderwall.com/mtchavez/endorsecount.png)](http://coderwall.com/mtchavez)

## Install

    pip install al_papi

## Usage

Configure your api key to be used to make requests:

    import al_papi

    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')

### POST

Post your keyword-engine-locale combination to the API once you have set your API key:

    import al_papi

    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')

    res = al_papi.Request.post({ "keyword" : "Centaur Stampede", "engine" : "bing", "locale" : "en-us" })

    if res.success
      print "Centaur High Hoof""
    else
      print "PAPI Fail"

### Priority POST

Post your keyword to the priority queue if you need results in a more timely manner:

    import al_papi

    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')

    res = al_papi.Request.priority_post({ "keyword" : "Druggie Scientist", "engine" : "bing", "locale" : "en-us" })

    if res.success
      print "Scientific Pontification"
    else
      print "Drugs are bad"

### GET

When you are ready to get your results you can do a GET request for your keyword-engine-locale combo:

    import al_papi

    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')

    res = al_papi.Request.priority_post({ "keyword" : "Canadian Wizards", "engine" : "bing", "locale" : "en-us" })

    if res.success
      print "Wizardry Is Sexy"
    else
      print "No magic, eh?"


### Response

When making an API request a response object is returned with any errors, http response code and http reponse body.

    import al_papi

    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')

    res = al_papi.Request.priority_post({ "keyword" : "Canadian Wizards", "engine" : "bing", "locale" : "en-us" })

    # Errors:
    # Returns an array of error objects.
    res.errors

    for err in res.errors:
      print err.message
      print err.code

    # Success:
    # Returns true or false if request was successful or not.
    res.success

    # Body:
    # Returns body of response.
    # On GET requests the body will be a hash of your results if successful.
    res.body

    # Code:
    # Returns http response code.
    # 204: On GET requests when no data is available yet
    # 200: Successful
    # 401: Invalid api key
    # 500: Server Error
    res.code

    # Over Limit:
    # Returns true or false if over hourly limit
    res.over_limit

    # Suspended:
    # Returns true or false if your account has been suspended
    res.suspended

## Web Insight

## Description

Web Insight queue takes a URL for the Partner API to scrape and parse out high level insight about the page
and return the results to your callback URL passed in or set for your account.

## POST

Post the URL of the page you want to gain insight into and the callback URL knowing when your results are
ready to get.

    import al_papi
    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')
    res = al_papi.WebInsight.post({"url" : "http://www.qwiki.com", "callback" : "http://your-callback.com"})

## GET

When your results are ready to get you will receive a callback that contains the information on how
to get the insight on your URL. In the callback you should receive a date_created and time_created to use
in your get request. You will also use your original URL posted.

    import al_papi
    al_papi.Config.setup('yR43BtRDjadfavXy6a4aK3')
    res = al_papi.WebInsight.post({"url" : "http://www.qwiki.com", "date_created" : "2012-06-14", "time_created" : "01:50"})

## Extras

### Engines

Supported engines are Google, Yahoo and Bing. To get a list of supported engines run the following:

    import al_papi

    al_papi.Engines.all

### Locales

Supported locales differ by the engine being used. In order to make sure you are using a supported locale
for the engine you are posting a keyword to there is a locales class to help you:

    import al_papi

    al_papi.Locales.supported # returns an array of locales for the default engine Google
    al_papi.Locales.supported 'bing' # for other engines pass in the engine name
    al_papi.Locales.supported 'yahoo'

## License

Written by Chavez

Released under the MIT License: http://www.opensource.org/licenses/mit-license.php
