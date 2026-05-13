import streamlit as st
from streamlit import config
import streamlit
from openai import OpenAI
import json
import st_yled
st_yled.init()




client = OpenAI(
    api_key= st.secrets['OPENAIKEY']
)

client = Youtube(
    api_key= st.secrets['YOUTUBEKEY']
)


st.tite('SAATFYC')
st.caption('Finds what you want!')

with st.sidebar:
    st.header('Filters')
    views_tier = [
        "10",
        "100",
        "1000",
        "10 000",
        "100 000",
        "500 000",
        "1 000 000,"
        "5 000 000,"
        "10 000 000+",
    ]
    min_views = st.selectbox("Minimum views", views_tier, index=0)

    subscriber_tier = [
               "10",
        "100",
        "1000",
        "10 000",
        "100 000",
        "500 000",
        "1 000 000,"
        "5 000 000,"
        "10 000 000+", 
    ]
    min_subs = st.selectbox("Minimum subscribers", subscriber_tier, index=0)

Prompt = st.text_input("Tell me what you want, I find.")
system_prompt = '''You will receive a prompt from the user requestion you to find a specific type of youtube video. Use relevant keywords in the user prompt or create your own keywords that fits the prompt. The youtube API key will give you a list of videos containing:
- Title
- Channel
- views
- subscribers
- link to the video
Choose 3 of the videos that the youtube API key gave you which fits the requirement of views and subscribers selected by the user, and display them in Json format:
"title": "",
"video_url": "",
"channel_name": "",
"view_count": number,
"channel_subscriber_count": number,
"score": number,
"reason": ""
'''



