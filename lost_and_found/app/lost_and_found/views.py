from . import lost_and_found
from flask import request, render_template, jsonify, redirect
from .models import LostAndFoundState, LostAndFound, Admin
from urllib.parse import quote
from ..wx import wx_models
from app import config, db
import ast


@lost_and_found.route('/index', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        code = request.args.get('code')
        openid = request.args.get('openid')
        nickname = request.args.get('nicknama')
        sex = request.args.get('nickname')
        url = quote(request.url)
        if code:
            url = wx_models.get_wx_permission(code)
            return redirect(url % ('index'))
        if openid is None:
            return redirect(
        config.DevConfig.CODE_URL %
        (config.DevConfig.appID, url, 'snsapi_userinfo', 'STATE'))

        if openid:
            info = LostAndFound.get_main_list(LostAndFoundState.NORMAL, 30)
            return render_template('index.html',
                                   openid=openid,
                                   nickname=nickname,
                                   sex=sex,
                                   appid=config.DevConfig.appID,
                                   info=info)

    if request.method == 'POST':
        data = request.form.get('value')
        if bool(data['state']):
            return
        else:
            state = LostAndFoundState.DELETE
            LostAndFound.set_state(id, state)
            return jsonify({'state':200,'msg':'删除成功'})



@lost_and_found.route('/release', methods=('GET', 'POST'))
def release():
    openid = request.args.get('openid')
    nickname = request.args.get('nickname')
    if openid is None:
        return render_template('error.html')

    if request.method == 'POST':
        user_id = openid
        article = request.form.get('article_name')
        receive_name = request.form.get('receive_name', 'None')
        send_name = request.form.get('send_name')
        content = request.form.get('content')
        lost_or_found = request.form.get('status')
        is_show_head = request.form.get('is_show_head', False)

        is_show_head = True if is_show_head == 'true' else False

        submit_times = LostAndFound.get_today_send_num_by_user_id(user_id)
        if submit_times > 5:
            err_msg = '今天发布的次数太多了，请改天再来'
            return jsonify({'state': 502, 'msg': err_msg})

        lostAndFound = LostAndFound(
            user_id,
            lost_or_found,
            article,
            send_name,
            content,
            is_show_head
        )
        if receive_name:
            lostAndFound.receive_name = receive_name
        db.session.add(lostAndFound)
        db.session.commit()

        return jsonify({'state': 200, 'msg': "提交成功，等待管理员审核"})

    return render_template('release.html',openid=openid,appid = config.DevConfig.appID)


@lost_and_found.route('/admin', methods=('GET', 'POST'))
def admin():
    url = quote(request.url)
    appid = config.DevConfig.appID
    if request.method == 'GET':
        type = request.args.get('type')
        code = request.args.get('code')
        openid = request.args.get('openid')
        if type == 'test':
            info = LostAndFound.query.filter_by(state=0).all()
            return render_template('admin.html', info=info, openid=openid)
        if code:
            url = wx_models.get_wx_permission(code)
            return redirect(url % ('admin'))

        if openid is None:
            return redirect(
        config.DevConfig.CODE_URL %
        (config.DevConfig.appID, url, 'snsapi_userinfo', 'STATE'))

        if Admin.query.filter_by(user_id=openid).first():
            info = LostAndFound.query.filter_by(state=0).all()
            return render_template('admin.html', info=info, openid=openid, appid=appid)

        else:
            return render_template('error.html')
    if request.method == 'POST':
        data = request.form.get('value')
        data = ast.literal_eval(data)
        id = data['id']
        user_id = ['user_id']
        if bool(data['state']):
            state = LostAndFoundState.NORMAL
            LostAndFound.set_state(id, state)
            return jsonify({'state': 200, 'msg': '已通过'})
        else:
            state = LostAndFoundState.DELETE
            LostAndFound.set_state(id, state)
            return jsonify({'state': 200, 'msg': '已打回'})


