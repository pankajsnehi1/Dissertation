#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "85285056-jk7QlaHO0DZHmvbGxsJqFmX44MtkLFStiTl8CBV2s"
access_token_secret = "n9pfItpAKqf6hPL8jFGLoRt4TsiSt1AnpawlBKbX8yMKr"
consumer_key = "l3m0ZysbUSq68ijZ8YiyaQlcs"
consumer_secret = "jpozK0XzVNyZWGMLQelxwzbuhK5y9ovQ4tbxgFYA6p0uS1cHWW"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['BP'])
