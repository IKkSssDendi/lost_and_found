from . import lost_and_found
from flask import request,render_template,jsonify,redirect
from .models import LostAndFoundState,LostAndFound
from urllib.parse import quote
from ..wx import wx_models
import time
from app import config

@lost_and_found.route('/index',methods=('GET','POST'))
def index():
    if request.method == 'GET':
        code = request.args.get('coed')
        openid = request.args.get('openid')
        nickname = request.args.get('nickname')
        sex = request.args.get('nickname')
        if code :
            url = wx_models.get_wx_permission(code)
            return redirect(url)
        if openid :
            return render_template('index.html',
                                   openid=openid,
                                   nickname=nickname)
        url = quote(request.url)
        return redirect(config.DevConfig.CODE_URL % config.DevConfig.appID,url,'snsapi_userinfo','')

@lost_and_found.route('/release',methods=('GET','POST'))
def release():
    if request.method == 'GET':
        return render_template('release.html')
    if request.method == 'POST':
        user_id = request.form.get('user_id',None)
        article = request.form.get('article')
        receive_name = request.form.get('recevie_name')
        send_name = request.form.get('send_name')
        content = request.form.get('content')
        lost_or_found = request.form.get('status')
        is_show_head = request.form.get('is_show_head',False)

        is_show_head = True if is_show_head == 'true' else False

        submit_times = LostAndFound.get_today_send_num_by_user_id(id)
        if submit_times > 5 :
            err_msg = '今天发布的次数太多了，请改天再来'
            return jsonify({'state': 502, 'msg': err_msg})

        lostAndFound = LostAndFound()

        lostAndFound.user_id = user_id
        lostAndFound.article = article
        lostAndFound.receive_name = receive_name
        lostAndFound.send_name = send_name
        lostAndFound.content = content
        lostAndFound.lost_or_found = lost_or_found
        lostAndFound.is_show_head = is_show_head
        lostAndFound.save()
        return jsonify({'state': 200, 'msg': "提交成功，等待管理员审核"})



