import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

from yt_channelVideo_stats import yt_channel_vid_statistic
from googleapiclient.discovery import build
api_key = "AIzaSyDqYcV4mJWQImAteWnLeIzVgO4X9fO-mIY"
#api_key = "AIzaSyAQ5NOVTp3LuGQZTb3RC_RREpTe3JGpvdg"
youtube = build("youtube", "v3", developerKey=api_key)

 
def convertJson_Pd(file_path):
    with open(file_path, 'r') as file:
        data_dict = json.load(file)

    final_dict = {}
    for key, value in data_dict.items():
        channel_name = value["Channel_name"]
        channel_id = value["Channel_id"]
        for i in value["Video_statistic"]:
            titles = ''.join(i["title"])
        for item in value["Video_statistic"]:
            descriptions = ''.join(item["description"])
        categories = value["Channel_Statistic"]["Categories"]
        keywords = value["Channel_Statistic"]["Keywords"]
        manual_category = value["Channel_Statistic"]["Manual_category"]

        final_dict[channel_id] = {
            "channel_name": channel_name,
            "titles": titles,
            "descriptions": descriptions,
            "categories": categories,
            "keywords": keywords,
            "manual_category": manual_category
        }

    df= pd.DataFrame(final_dict)
    df =df.transpose()
    return df

def convertDictPd(input_dic):
    final_dict = {}
    value = input_dic
    channel_name = value["Channel_name"]
    channel_id = value["Channel_id"]
    for i in value["Video_statistic"]:
        titles = ''.join(i["title"])
    for item in value["Video_statistic"]:
        descriptions = ''.join(item["description"])
    categories = value["Channel_Statistic"]["Categories"]
    keywords = value["Channel_Statistic"]["Keywords"]
    manual_category = value["Channel_Statistic"]["Manual_category"]

    final_dict[channel_id] = {
        "channel_name": channel_name,
        "titles": titles,
        "descriptions": descriptions,
        "categories": categories,
        "keywords": keywords,
        "manual_category": manual_category
    }
    input_pd = pd.DataFrame(final_dict)
    input_pd  =input_pd .transpose()
    return input_pd 


def tfIdfTest(top_n, input_pd, db_pd):

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(db_pd['descriptions'])

    r_dict = {}
    for i in range(len(input_pd)):
        name = input_pd.iloc[i]['channel_name']
        user_input = input_pd.iloc[i]['descriptions']
        user_tfidf = vectorizer.transform([user_input])

        # Step 5: Similarity Calculatio
        cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()

        top_indices = cosine_similarities.argsort()[:-top_n-1:-1]
        recommended_channels = db_pd.iloc[top_indices].index.tolist()
        r_dict[name] = recommended_channels

    return r_dict

def cleantxt(jsondata, key_dict):
    f_dict ={}
    for key, item in key_dict.items():
        key_list = item
    for key in key_list:
        for channel_id in jsondata:
            if key == channel_id:
                channel_name = jsondata[key]["Channel_name"]
                channel_info =jsondata[key]["Channel_Statistic"]
                subs = channel_info['Subscribers']
                totalViews =  channel_info['Views']
                totalVideos = channel_info["Total_videos"]  
                averageViews = int(int(totalViews)/int(totalVideos))
                f_dict[channel_name] = {'Channel_name': channel_name, 
                                   'Subscribers': subs, 
                                   'Totat_views':totalViews, 
                                   "Total_Videos": totalVideos,
                                   "Average_views":averageViews
                                   }
            else:   
                pass
    df = pd.DataFrame(f_dict)
    df = df.transpose()
    return df

if __name__ == "__main__":

    #FINDING THE TOP 5 MOST SIMILIAR CHANNELS IN THE DATABASE WHEN WHEN INPUT A COMPLETETLY NEW CHANNEL.
    
    
    #Find input dictionary to pd 
    channel_url = "https://www.youtube.com/@CiottiFPV"
    input = yt_channel_vid_statistic(channel_url, api_key, youtube, my_categ="whoop")
    input_dic = input.final_stats()
    f_input_pd = convertDictPd(input_dic)

    # conver json to pd
    db_file_path = '/Users/seanyoo/Desktop/recommending_similiarity/json/yt_channelVideo_stats.json'
    f_db_pd = convertJson_Pd(db_file_path)
    
    top_n=10
    trial = tfIdfTest(top_n, f_input_pd, f_db_pd)
    with open('/Users/seanyoo/Desktop/recommending_similiarity/json/yt_channelVideo_stats.json') as json_file:
        jsondata = json.load(json_file) 
    clean = cleantxt(jsondata, trial)