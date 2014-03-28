from TwitterSearch import *
import rethinkdb as r
r.connect('localhost', 28015).repl()

twittertweets = r.db('tweets').table('twittertweets')
counter = 0 #Start of counter, better to save / load from file
#Acknowledgments: Most of Twitter Search code from: https://pypi.python.org/pypi/TwitterSearch/ (Twitter Search Example)
#Modified python script by Tsubasa Kato (@stingraze) 

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['supercomputer']) #Query to send to Twitter API
    tso.setLanguage('en') # we want to see English tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
         consumer_key='xxxx',
         consumer_secret='xxxx',
         access_token='xxxx',
         access_token_secret='xxxx')



    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
	counter = counter + 1
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
	twittertweets.insert({"id": counter, "user": tweet['user']['screen_name'], "tweet": tweet['text']}).run() #Inserts tweets to RethinkDB


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
                 
