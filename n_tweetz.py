import os
import tweepy
import click

KEY = os.environ.get('TWITTER_KEY')
SECRET = os.environ.get('TWITTER_SECRET')


@click.command()
@click.argument('n')
@click.argument('username')
def get_n_tweetz(n, username):
    """Get the last n Tweets of a user
    \b
    N           Number of tweets to return
    USERNAME    Username on Twitter
    """
    auth = tweepy.OAuthHandler(KEY, SECRET)
    api = tweepy.API(auth)
    resp = api.user_timeline(username, count=n)

    click.secho('RT\tSTAR\tTWEET', bold=True)
    for index, status in enumerate(resp):
        click.secho(str(status.retweet_count)+"\t",
                    nl=False, fg='yellow', bold=True)
        click.secho(str(status.favorite_count)+"\t",
                    nl=False, fg='blue', bold=True)
        click.secho(status.text, fg='white')

if __name__ == '__main__':
    get_n_tweetz()
