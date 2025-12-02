from fastapi import APIRouter, BackgroundTasks
from app.scraper.twitter_scraper import scrape_twitter
from app.nlp.sentiment_analysis import analyze_sentiment
from app.nlp.topic_detection import detect_topics
from app.nlp.text_processing import clean_text, normalize_text
from app.database.mongodb import init_db,get_posts


router = APIRouter(
    tags=["api"]
)
@router.post("/scrape_twitter")
async def start_scraping(background_tasks: BackgroundTasks):
    background_tasks.add_task(process_and_save_tweets)
    return {"message": "Twitter scraping started in the background."}
async def process_and_save_tweets():
    db=await init_db()
    tweets=scrape_twitter("depression",15,True)
    for _,tweet in tweets.iterrows():
        try:
            tweet_content=tweet['content']
            cleaned_text=clean_text(tweet_content)
            normalized_text=normalize_text(cleaned_text)
            sentiment=analyze_sentiment(normalized_text)
            topics=detect_topics(normalized_text)

            await db.posts.insert_one({
                "tweet_id": tweet["id"],
                "username": tweet["username"],
                "date": tweet["date"],
                "text": tweet_content,
                "cleaned_text": cleaned_text,
                "normalized_text": normalized_text,
                "sentiment": sentiment,
                "topics": topics,
                "like_count": int(tweet["like_count"]),
                "retweet_count": int(tweet["retweet_count"])                
            })
            print(f"Saved Tweet {tweet['id']} to database.")
        except Exception as e:
            print(f"Error Processing Tweet  {e}")
    return {"message": "Tweet processing and saving completed."}
@router.get("/posts")
async def get_all_posts(limit: int = 100):
    posts = await get_posts(limit)
    return {"posts": posts}
