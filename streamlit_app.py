import streamlit as st
import requests
import pandas as pd

@st.cache_data(ttl=60*60*12)
def fetch_emojis():
    resp = requests.get(
        'https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json')
    json = resp.json()
    codes, emojis = zip(*json.items())
    return pd.DataFrame({
        'Emojis': emojis,
        'Shortcodes': [f':{code}:' for code in codes],
    })

'''
# Streamlit emoji shortcodes

Below are all the emoji shortcodes supported by Streamlit.

Shortcodes are a way to enter emojis using pure ASCII. So you can type this `:smile:` to show this
:smile:.

(Keep in mind you can also enter emojis directly as Unicode in your Python strings too — you don't
*have to* use a shortcode.)
'''

st.info(
    """
        In addition to the standard emojis listed below, add a little Streamlit
        flair with `:streamlit:` -> :streamlit: for Streamlit version 1.40.0
        and later.
    """
)

emojis = fetch_emojis()

st.table(emojis)
