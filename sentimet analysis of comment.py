from textblob import TextBlob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_sentiment(comment_list):
    list = []
    for comment in comment_list:
        blob = TextBlob(comment)
        sentiment = blob.sentiment.polarity
        #return sentiment
        if sentiment > 0:
            list.append('Positive')
        elif sentiment < 0:
            list.append("Negative")
        else:
            list.append('Neutral')
    return list

if __name__ == "__main__":
    comment_data = pd.read_csv("comments.csv")
    #print(analyze_sentiment(data["comment"]))
    comment_data["sentiment"] = analyze_sentiment(comment_data["comment"])
    #print(data)
    comment_data.to_csv("comments.csv")
    print(comment_data["sentiment"].value_counts())
    plt_data_set= list(comment_data["sentiment"].value_counts())
    labels=["","",""]

    fig, ax = plt.subplots()
    ax.pie(plt_data_set,labels =labels )
    plt.show()










