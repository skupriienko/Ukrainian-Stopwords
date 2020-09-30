import pandas as pd

stopwords_ua = pd.read_csv("stopwords_ua.txt", header=None, names=['stopwords'])
stop_words_ua = list(stopwords_ua.stopwords)

def clean_text(text):
    text = "".join([word for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [word for word in tokens if word not in stop_words_ua]
    return text


# articles_text_list is your list with text

# create your dataframe with a text column like this one from your list
data = pd.DataFrame(articles_text_list, columns=['article_title', 'txt', 'article_source_url', 'url_of_article', 'article_keywords', 'article_publish_date'])
data.sort_values(by='url_of_article') 

# data["txt"] is your text column

# remove stopwords
# try it after preprocessing text
data['body_text_nostop'] = data["txt"].apply(lambda x: clean_text(x.lower()))