import  string
from collections import Counter
import matplotlib.pyplot as plt
#load data
text = open ('text.txt' , encoding='utf-8').read()
#print(text)
#clean data

lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)

#Tokenization and Stop Words

tokenized_words = cleaned_text.split()
#print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []

for words in tokenized_words:
    if words not in stop_words:
        final_words.append(words)

#print(final_words)

#Algorithm for Emotion and Text Analysis
emotion_liste =[]
with open('emotions.txt' ,'r') as file :
    for line in file:
        clear_line = line.replace("\n" ,'').replace(",",'').replace("'",'').strip()
       # print(clear_line)
        words , emotion = clear_line.split(':')
        #print(  "Word :"+words+"  "+"Emotion :"+ emotion)

        if words in final_words:
            emotion_liste.append(emotion)

print (emotion_liste)
w = Counter(emotion_liste)
#print(w)

#Emotions in a Graph using Matplotlib

#plt.bar(w.keys() , w.values())
#plt.savefig('graph.png')
#plt.show()

fig, ax1 =plt.subplots()
ax1.bar(w.keys() , w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()