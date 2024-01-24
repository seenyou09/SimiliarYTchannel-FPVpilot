'''
We extract information that we need from the Json file to excel file
'''

import json
import pandas as pd
from datetime import datetime
from pathlib import Path

def average_days_between_dates(date_list):
    # Convert each date-time string into a datetime object
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    datetime_list = [datetime.strptime(date_str, date_format) for date_str in date_list]

    # Calculate time differences between consecutive dates
    intervals = [datetime_list[i + 1] - datetime_list[i] for i in range(len(datetime_list) - 1)]

    # Calculate the total number of days between all pairs of dates
    total_days = sum(interval.days for interval in intervals)

    # Calculate the average days
    if len(intervals) > 0:
        average_days = total_days / len(intervals)
    else:
        average_days = 0

    return average_days * int(-1)

# Example usage:
date_list = ["2023-07-07T22:58:25Z", "2023-07-15T10:30:00Z", "2023-07-25T18:45:12Z"]
avg_days = average_days_between_dates(date_list)
print("Average days between dates:", avg_days)

def findValueOfLike(likeDislikeList):
    total_ratio = 0

    for item in likeDislikeList:
        like = int(item[0])
        dislike = int(item[1])

        if dislike != 0:
            value_ratio = like / dislike
        else:
            value_ratio = like

        total_ratio += value_ratio

    if len(likeDislikeList) != 0:
        average_ratio = total_ratio / len(likeDislikeList)
    else:
        average_ratio = 0

    return average_ratio

# Example usage:
likeDislikeList = [(10, 2), (5, 1), (8, 3), (12, 4)]
avg_ratio = findValueOfLike(likeDislikeList)
print("Average value ratio of likes to dislikes:", avg_ratio)


def extract_json_key(file_path):
    # Read JSON data from the file
    with open(file_path, 'r') as file:
        data = json.load(file)
    f_dict = {}
    for key, value in data.items():
        channel_name = value["Channel_name"]
        channel_id = value["Channel_id"]
        channel_stats = value["Channel_Statistic"]
        subscribers = channel_stats["Subscribers"]
        manual_category = channel_stats["Manual_category"]
        views = channel_stats["Views"]
        numVideos = channel_stats['Total_videos']
        avg_views = int(views)/int(numVideos)
        date_list = []
        dislikeLike_list = []
        video_stats = value["Video_statistic"]
        for item in video_stats:
            date_list.append(item["published"])
            like = item["like_count"]
            dislike = item["dislike_count"]
            LikeDislike = (like, dislike)
            dislikeLike_list.append(LikeDislike)
        avg_int = average_days_between_dates(date_list)
        valueLike = findValueOfLike(dislikeLike_list)
        f_dict[channel_id] = (channel_name, channel_id, subscribers, views, numVideos, avg_views, avg_int, valueLike,manual_category)
    return f_dict








# File path of the JSON file
relative_path = Path('json/yt_channelVideo_stats-Database.json')

# Get the absolute path for the relative path
absolute_path = relative_path.resolve()
f_dict = extract_json_key(absolute_path)
# Create DataFrame from the dictionary
df = pd.DataFrame(f_dict)

# Transpose the DataFrame
df = df.transpose()

# Print the DataFrame
print(df)

# Save DataFrame to Excel file
df.to_excel("fpvDroneInfluencerDataframe-final.xlsx", index=False)
