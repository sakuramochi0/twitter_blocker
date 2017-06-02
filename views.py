import tweepy

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings

from .models import User

api_key = settings.TWITTER_BLOCKER_API_KEY
api_secret = settings.TWITTER_BLOCKER_API_SECRET

user_ids = [
    870250103004577792, # @xxxx_xxx_george ネタバレアカウント(一部伏せ字)
    
]

def index(request):
    block_count = User.objects.count()
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(user_id=user_id)
    except:
        user = None
    return render(request, 'twitter_blocker/index.html',
                  {'user': user, 'user_id': user_id, 'block_count': block_count})

def blocked(request):
    return render(request, 'twitter_blocker/blocked.html')

def connect(request):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth_url = auth.get_authorization_url()
    request.session['request_token'] = auth.request_token
    return redirect(auth_url)

def callback(request):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    session = request.session.keys()
    auth.request_token = request.session['request_token']
    access_token, access_token_secret = auth.get_access_token(request.GET['oauth_verifier'])
    api = tweepy.API(auth)
    me = api.me()

    # spam report & block
    blocked_user_ids = []
    for user_id in user_ids:
        api.report_spam(user_id=user_id)
        blocked_user_ids.append(user_id)
    blocked_user_ids = ','.join(list(map(str, blocked_user_ids)))

    try:
        user_id = me.id
        user = User.objects.get(user_id=user_id)
    except:
        user = User.objects.create(
            user_id=me.id,
            screen_name = me.screen_name,
            oauth_key = access_token,
            oauth_secret = access_token_secret,
            blocked_user_ids = blocked_user_ids,
        )
        user.save()
    
    # save login state to session
    request.session['user_id'] = me.id

    return redirect(reverse('blocked'))

