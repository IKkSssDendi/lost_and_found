import requests
from app import config
import json
import logging

def get_wx_permission(code):
    url = config.DevConfig.ACCESS_TOKEN_URL % (
        config.DevConfig.appID,
        config.DevConfig.appSerect,
        code
    )
    try:
        r = requests.get(url)

    except Exception as e:
        logging.warning(u'获取授权失败:%s' % e)
        return {}
    else:
        content = str(r.content,encoding='utf8')
        content = json.loads(content)
        access_token = content['access_token']
        expires_in = content['expires_in']
        refresh_token = content['refresh_token']
        openid = content['openid']
        scope = content['scope']
        data = get_user_data(access_token,openid)
        url = '/LostAndFound/%s' + '?openid=%s&nicknama=%s&sex=%s' % (openid,data['nickname'],data['sex'])

        return url

def get_base_access_token():
    url = config.DevConfig.ACCESS_TOKEN_URL % (
        'client_credential',
        config.DevConfig.appID,
        config.DevConfig.appSerect
    )
    try:
        r = requests.get(url)

    except Exception as e:
        logging.warning(u'获取base_accesee_token失败:%s' % e)
        return {}
    else:
        content = json.loads(str(r.content,encoding='utf8'))
        if content['errcode'] and content['errcode'] != 0:
            return content
        else:
            base_access_token = content['access_token']

    return base_access_token

def get_user_data(access_token,openid,lang='zh_CN'):
    url = config.DevConfig.GET_USER_DATA_URL % (access_token,openid,lang)
    r = requests.get(url)
    content = json.loads(str(r.content,encoding='utf8'))
    nickname = content['nickname']
    if content['sex'] == '1':
        sex = '男性'
    elif content['sex'] == '2':
        sex = '女性'
    else:
        sex = '未知'

    return {
        'nickname':nickname,
        'sex':'sex'
    }






