import sys
import pandas as pd
if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

topic = "#elpiscosiesperuano"
start_date = "2016-01-01"
end_date = "2017-05-28"
num_tweets = 1200

tweetCriteria = got.manager.TweetCriteria().setQuerySearch(topic).setSince(start_date).setUntil(end_date).setMaxTweets(num_tweets)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

tList = []

for t in tweets:
    tList.insert(-1, [t.username, t.text])

df = pd.DataFrame(tList)
df.to_csv('tweets.csv', index=False)