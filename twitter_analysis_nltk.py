import GetOldTweets3 as got
import  string
from nltk.corpus import  stopwords
from nltk.tokenize import  word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt

def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setUsername("nike") \
        .setSince("2019-08-01") \
         .setUntil("2020-02-28") \
        .setMaxTweets(1000)
    #list of object gets stored in 'tweets' variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text]  for tweet in tweets]
    return  (text_tweets)

text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0 , length):
    text = text_tweets[i][0]+" "+text

#print(text)
#clean data

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)

#Tokenization and Stop Words
tokenized_words = word_tokenize( cleaned_text ,"english")

#print(tokenized_words)
final_words = []
for words in tokenized_words:
    if words not in stopwords.words('english'):
        final_words.append(words)

#print(final_words)

#Algorithm for Emotion and Text Analysis

emotion_liste =[]
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg =score['neg']
    pos = score['pos']
    emotion_liste.append(score.keys())
    if neg > pos :
        print("Negative ")
    elif pos >neg :
        print ("Positive")
    else :
        print ("neutral")

sentiment_analyse(cleaned_text)
print (emotion_liste)
w = Counter(list(emotion_liste.keys()))

fig, ax1 =plt.subplots()
ax1.bar(w.keys() , w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()