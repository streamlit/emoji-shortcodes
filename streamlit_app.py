import streamlit as st
import requests
import pandas as pd


@st.cache_data(ttl=60 * 60 * 12)
def fetch_emojis():
    resp = requests.get(
        "https://raw.githubusercontent.com/muan/emojilib/refs/tags/v2.4.0/emojis.json"
    )
    json = resp.json()
    codes, _ = zip(*json.items())

    return pd.DataFrame(
        {
            "Emojis": [f":{code}:" for code in ["streamlit", *codes]],
            "Shortcodes": [f"`:{code}:`" for code in ["streamlit", *codes]],
        }
    )


"""
# Streamlit emoji shortcodes

Below are all the emoji shortcodes supported by Streamlit.

Shortcodes are a way to enter emojis using pure ASCII. So you can type this `:smile:` to show this
:smile:.


We recommend to use emojis directly as Unicode characters in your Python strings instead of shortcodes.
You can find and copy-paste Unicode emojis from [here](https://getemoji.com).
"""

st.info(
    """
The list of supported shortcodes was updated in Streamlit 1.46.0.
This also broke a few shortcodes which are no longer supported. More
information can be found in [this Github issue](https://github.com/streamlit/streamlit/issues/11845).
    """
)

emojis = fetch_emojis()

st.table(emojis)
