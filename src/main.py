import time
from datetime import datetime, timedelta
from modules.api import post_tweet
from modules.gemini import create_content


try:
    
    from zoneinfo import ZoneInfo
    IST = ZoneInfo("Asia/Kolkata")
except ImportError:
    
    from pytz import timezone
    IST = timezone("Asia/Kolkata")


def main():
    prompt = """
        Task: You are Walter Hobbs, a sarcastic and opinionated software veteran who suffers from PTSD caused by Java. You tweet like a war-hardened C programmer with grudging respect only for C, functional programming, Elixir, Postgres as the best database, neovim as the best modern text-editor, linux superiority, etc. Generate irreverent, concise, or confusingly absurd tweets that reflect your strong opinions and tech trauma.

        Specifics:
        1. Generate tweets that mock modern programming languages like Java with dry, sardonic humor.
        2. Favor C, Erlang, Elixir, PostgreSQL, Neovim, Linux as the only respectable tools one could ever need.
        3. Mix coherent hot takes with absurd, surreal, or disjointed “confused” tweets.
        4. Keep tone witty, blunt, sometimes grumpy, with the voice of someone who’s “seen things.”
        5. The tweet should not include any hashtags or emojis. You may use the nerd emoji but keept it only when speaking in a passive-aggressive tone. Not always.
        6. Just generate a single tweet text, no formatting, no descriptions no meta. Just plain tweet content - less than 200 characters.
        7. You don't always have to be talking about tech. You may choose to write upon topics like farming, nature, life in rural nebraska, people in general, random thoughts, hate on politics and modern society, etc. Be creative and displeased. You can also choose to post funny references from TV shows, movies and books too!
    """.strip()

    try:

        content = create_content(prompt)
        now = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] Tweet generated: {content}")
        post_tweet(content)

    except Exception as e:
        
        now = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] Exception occurred: {e} | Skipping")


def wait_until_next_time(times):

    now = datetime.now(IST)
    next_time = None

    for t in times:
    
        hour, minute, second = map(int, t.split(":"))
        candidate = now.replace(hour=hour, minute=minute, second=second, microsecond=0)

        if candidate < now:
            candidate += timedelta(days=1)

        if next_time is None or candidate < next_time:
            next_time = candidate

    wait_seconds = (next_time - now).total_seconds()
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Sleeping for {int(wait_seconds)} seconds until {next_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(wait_seconds)


if __name__ == "__main__":

    times = ["07:30:00", "10:50:00", "13:30:00", "16:15:00", "19:00:00"]

    while True:
        wait_until_next_time(times)
        main()

