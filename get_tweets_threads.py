import twitter
import pandas as pd
import os
import concurrent

consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_token_secret = os.environ['access_token_secret']


def get_tweets_of_user(user):
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_token_secret)
    tweets = api.GetUserTimeline(screen_name=user, count=200)
    texts = [tweet.text for tweet in tweets]
    return texts


def save_texts_in_file(file_name, texts):
    tweets_df = pd.DataFrame({"tweets": texts})
    tweets_df.to_excel(file_name)


def read_text_file(file_name):
    with open(file_name, 'r', encoding="utf8") as my_file:
        lines = my_file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def save_user_tweets(user):
    print(f"started {user}")
    if not os.path.isfile(f"tweets\\right\{user}.xlsx"):
        texts = get_tweets_of_user(user)
        print(len(texts))
        save_texts_in_file(f"tweets\\right\{user}.xlsx", texts)
    print(f"finished {user}")


if __name__ == '__main__':
    right_users = read_text_file("users//right.txt")
    # left_users = read_text_file("users//left.txt")

    executor = concurrent.futures.ProcessPoolExecutor(10)
    futures = [executor.submit(save_user_tweets, user) for user in right_users]
    concurrent.futures.wait(futures)

    # print("right")
    # for user in right_users:
    #     print(user)
    #     if not os.path.isfile(f"tweets\\right\{user}.xlsx"):
    #         texts = get_tweets_of_user(user)
    #         print(len(texts))
    #         save_texts_in_file(f"tweets\\right\{user}.xlsx", texts)
    #     print()

    # print("left")
    # for user in left_users:
    #     print(user)
    #     if not os.path.isfile(f"tweets\\left\{user}.xlsx"):
    #         texts = get_tweets_of_user(user)
    #         print(len(texts))
    #         save_texts_in_file(f"tweets\\left\{user}.xlsx", texts)
    #     print()