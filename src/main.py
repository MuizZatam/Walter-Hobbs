from modules.api import post_tweet


def main():

    content = "We wrote C programs that ran where we damn well told them to. Still don’t get how those Java people sleep at night saying compile once, run everywhere. It’s literally Compile once, debug everywhere."

    post_tweet(content)


if __name__ == "__main__":

    main()
