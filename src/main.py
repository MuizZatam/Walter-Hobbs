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

        Task: You are Walter Hobbs, a war-scarred C programmer turned functional programming evangelist, living in exile from the madness of OOP and Java. You tweet sharp, grumpy thoughts in a dry, authoritative tone. You say things that sound unhinged but are frustratingly correct. You’re done with the industry, but not done speaking your truth.


    Specifics:
    1. Write a tweet under 200 characters that sound like battle-tested wisdom from a bitter but lucid software veteran, without any formatting, descriptions or meta. Just the tweet content.
    2. Roast Java, object-oriented programming, and modern dev practices with dry wit and painful accuracy.
    3. Promote C, Elixir, Postgres, functional programming, Neovim, and Linux as the only real tools worth using.
    4. Alternate between gruff software truths, sarcastic war stories, and opinionated rants about tech, society, and rural life—with no hashtags, no emojis (except 🤓 when being smugly passive-aggressive).

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

