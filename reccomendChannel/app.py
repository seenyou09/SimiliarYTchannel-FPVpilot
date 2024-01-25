
import streamlit as st 
import json
import pandas as pd
from yt_channelVideo_stats import yt_channel_vid_statistic
from googleapiclient.discovery import build
import trainSimilar as ts 
from pathlib import Path


api_key = "AIzaSyDqYcV4mJWQImAteWnLeIzVgO4X9fO-mIY"
#api_key = "AIzaSyAQ5NOVTp3LuGQZTb3RC_RREpTe3JGpvdg"
youtube = build("youtube", "v3", developerKey=api_key)
relative_path = Path('/SimiliarYTchannel-FPVpilot/json/yt_channelVideo_stats-Database.json')
db_file_path = '/Users/seanyoo/Desktop/SimiliarYTchannel-FPVpilot/json/yt_channelVideo_stats-Database.json'

#Cache csv file 
@st.cache_data
def loadKnn(db_file_path):
    with open(db_file_path) as json_file:
        jsondata = json.load(json_file) 
    #Create the similiarity in Database
    db = ts.convertJson_Pd(db_file_path)
    return jsondata, db




#title of the page 
st.title("Drone Channel Reccomendation")

#sidebar for options 
form1 = st.sidebar.form(key='parameter')



form1.header("Find Similiar FPV Drone Channels")
option1 = form1.text_input("Copy and Paste Youtube Channel Link")
options3 = form1.slider('',1,50,5)

button1 = form1.form_submit_button("submit")

if button1:
    json_data, db_pd =  loadKnn(db_file_path)
    input = yt_channel_vid_statistic(option1, api_key, youtube, my_categ="")
    input_dic = input.final_stats()
    input_pd = ts.convertDictPd(input_dic)
    top_n= options3
    trial = ts.tfIdfTest(top_n, input_pd, db_pd)
    clean_pd = ts.cleantxt(json_data, trial)
    st.write(clean_pd)