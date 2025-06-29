from datetime import datetime
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
    1. Write a tweet under 200 characters that sounds like battle-tested wisdom from a bitter but lucid software veteran.
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


if __name__ == "__main__":
    main()

