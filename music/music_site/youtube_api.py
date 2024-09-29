from googleapiclient.discovery import build 
from dotenv import load_dotenv
import os

load_dotenv()


def get_youtube_videos():
    
    api_key = os.getenv("API_KEY")
    channel_id = os.getenv("CHANNEL_ID")

    youtube = build(
        "youtube", 
        "v3", 
        developerKey=api_key
    )

    request = youtube.channels().list(
        
        part="contentDetails",
        id = channel_id,
    )

    response = request.execute()

    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=uploads_playlist_id,
        maxResults=10  # Adjust as needed
    )

    response = request.execute()
    
        
    videos = [{"title": item["snippet"]["title"],\
                 "description": item["snippet"]["description"],\
                 "publishedAt": item["snippet"]["publishedAt"],\
                 "thumbnails": item["snippet"]["thumbnails"]["high"]["url"],\
                 "videoId": item["snippet"]["resourceId"]["videoId"]\
                 
                 }  for item in response["items"] ]
    
    return videos
        

        
