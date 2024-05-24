import praw
import requests
import logging
import _bot_config_

logging.basicConfig(level=logging.INFO)

def index():
    reddit = praw.Reddit(
        username=_bot_config_.username,
        password=_bot_config_.password,
        client_id=_bot_config_.client_id,
        client_secret=_bot_config_.client_secret,
        user_agent=_bot_config_.user_agent,
    )

    subreddit = reddit.subreddit("testingground4bots")

    location = input("Choose a location: ")
    weather_data = get_weather_data(location)

    if weather_data:
        title = f"Weather in {location}"
        
        weather_info = f"Current temperature: {weather_data['current']['temp_c']}°C"

        submission_text = f"{title}\n\n{weather_info}"

        subreddit.submit(title, selftext=submission_text)
        
        logging.info("Post submitted successfully")
    else:
        logging.error("Failed to fetch weather data")


def get_weather_data(location):
    base_url = "http://api.weatherapi.com/v1"
    
    key = "api key"
    
    endpoint = f"{base_url}/current.json?key={key}&q={location}"
    
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        logging.error(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    index()
