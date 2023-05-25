import streamlit as st
from googleapiclient.discovery import build
import pandas as pd
def get_channel_details(channel_id,api_key):
    youtube = build('youtube', 'v3',developerKey=api_key)
    request = youtube.channels().list(
            part='statistics,snippet',
            id=channel_id
       )
    response = request.execute()
    return response
st.title("YouTube Channel Details")

channel_id_1 = st.text_input("Enter YouTube Channel ID 1", key="channel_id_1")

channel_details = None
details_retrieved = False
if st.button("Get Channel Details 1"):
    api_key = "AIzaSyCupMkd5xxo12-VQ14elxGTIfudiN3ezrI"
    channel_details = get_channel_details(channel_id_1, api_key)
    details_retrieved = True
    st.write(channel_details)
st.title("YouTube Channel Details")

channel_id_3 = st.text_input("Enter YouTube Channel ID",key="channel_id_3")

if st.button("Get Channel Details 3"):
    api_key = "AIzaSyCupMkd5xxo12-VQ14elxGTIfudiN3ezrI"
    channel_details = get_channel_details(channel_id_3, api_key)
    details_retrieved = True
    st.write(channel_details)
st.title("YouTube Channel Details")

channel_id_4 = st.text_input("Enter YouTube Channel ID", key="channel_id_4")

if st.button("Get Channel Details 4"):
    api_key = "AIzaSyCupMkd5xxo12-VQ14elxGTIfudiN3ezrI"
    channel_details = get_channel_details(channel_id_4, api_key)
    details_retrieved = True
    st.write(channel_details)

channel_data = {}
if details_retrieved:  # Check if channel details have been retrieved
    if st.checkbox("Select channel to migrate"):
        channel_data = {
            'channel_id': channel_id,
            'channel_name': channel_details['items'][0]['snippet']['title'],
            'subscriber_count': channel_details['items'][0]['statistics']['subscriberCount'],
            'video_count': channel_details['items'][0]['statistics']['videoCount']
        }
        st.write(channel_data)
else:
    st.warning("Please retrieve channel details first.")

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
api_service_name = "youtube"
api_version = "v3"
developer_key = "AIzaSyCupMkd5xxo12-VQ14elxGTIfudiN3ezrI"
youtube = build(api_service_name, api_version, developerKey=developer_key)
channel_id = "@madangowri" # replace with the ID of the channel you want to retrieve
part = "snippet,statistics" # specify the parts of the channel you want to retrieve

try:
    response = youtube.channels().list(
        part=part,
        id=channel_id
    ).execute()
    # process the response data as needed
except HttpError as e:
    print("An error occurred: %s" % e)
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["youtube_data"]
collection = db['youtube collections']
collection.insert_one(channel_data)
import pymongo
import mysql.connector

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['youtube_data']
collection = db['youtube collections']

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    host='localhost:3306',
    user='root',
    password='yogeshraj544yok',
    #database="yok"
)
mysql_cursor = mysql_conn.cursor()

# Retrieve data from MongoDB and insert into MySQL
for doc in collection.find():
    channel_id = doc['channel_id']
    channel_name = doc['channel_name']
    subscriber_count = doc['subscriber_count']
    video_count = doc['video_count']

    sql = "INSERT INTO channels (channel_id, channel_name, subscriber_count, video_count) VALUES (%s, %s, %s, %s)"
    values = (channel_id, channel_name, subscriber_count, video_count)
    mysql_cursor.execute(sql, values)

mysql_conn.commit()
mysql_cursor.close()
mysql_conn.close()




