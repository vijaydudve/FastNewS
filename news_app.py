import requests
import json
import time
import streamlit as st


st.set_page_config(page_title='FastNewS', page_icon='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAZTbfXi1cP-4R-bfKSXzIQ2Piqd9cX8cjIA&usqp=CAU')

def get_trending_news():
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3b8b2056a5eb4e66bb2e0a74762ef29a"
    news_data = requests.get(url).text
    # # print(news)
    news_json =json.loads(news_data)
    # # print(news_json["articles"])
    news=news_json["articles"]
    # # print(news)
    # for i in news:
    #      print(i["description"])
    #      # speak(i["description"])
    return news

def get_categorical_news(topic):
    url = "https://newsapi.org/v2/top-headlines?country=in&category={}&apiKey=3b8b2056a5eb4e66bb2e0a74762ef29a".format(topic)
    news_data = requests.get(url).text
    news_json = json.loads(news_data)
    news = news_json["articles"]
    return news

def display(newss, quantity):
    c = 0
    for i in newss:
        c += 1
        st.write('**({}) {}**'.format(c,i["title"]))
        if i["urlToImage"]:
            st.image(i["urlToImage"],use_column_width=True)
        else:
            st.image("data:image/png;base64,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",use_column_width=True)
        with st.expander(i["title"]):
            st.markdown('''<h6 style='text-align: justify;'>{}"</h6>'''.format(i['content']),unsafe_allow_html=True)
            st.markdown("[Read more at {}...]".format(i["url"]))
        st.success("Published Date: "+ i["publishedAt"].split("T")[0])
        if c >= quantity:
            break



def run():
    st.title("FastNewS: Small & Quick Summary")
    col1, col2, col3 = st.columns([3,5,3])
    with col1:
        st.write("")
    with col2:
        st.image("data:image/png;base64,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", use_column_width=False)
    with col3:
        st.write("")
    category = ['--Select--','Trending News','Specific domain News']
    cat = st.selectbox("Select Category",category)
    if cat==category[0]:
        st.warning('Please select the Category')
    elif cat==category[1]:
        st.subheader("Here is the trending news for you")
        news_count = st.slider('Number of news',min_value=5,max_value=15,step=1)
        news = get_trending_news()
        display(news,news_count)
    elif cat == category[2]:
        topics=['choose topic','health','sports','business','technology','entertainment']
        # st.subheader("choose your favorite topic")
        choosen_topic = st.selectbox("Choose Category",topics)
        if choosen_topic == topics[0]:
            st.warning("please choose topic")
        else:
            news_count = st.slider('Number of news', min_value=5, max_value=20, step=1)
            news = get_categorical_news(choosen_topic)
            if news:
                st.subheader("Here are your {} news".format(choosen_topic))
                display(news,news_count)
            else:
                st.error("No {} news found",format(choosen_topic))
run()