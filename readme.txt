
== OAuth Authentication ==
This mode of authentication is the new preferred way
of authenticating with Twitter.

The consumer keys can be found on your application's Details
page located at https://dev.twitter.com/apps (under "OAuth settings")

The access tokens can be found on your applications's Details
page located at https://dev.twitter.com/apps (located under "Your access token")

If the application settings are set for "Read and Write" then
this line should tweet out the message to your account's 
timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status('Hello World!')