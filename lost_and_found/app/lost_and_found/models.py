from app import db
import datetime
import time
from sqlalchemy import text
from sqlalchemy.sql import func


class LostAndFoundState():
    TOP = 2
    NORMAL = 1
    UNCHECK = 0
    DELETE = -1

    def __get__(self,instance,owner):
        return self.value


class LostAndFound(db.Model):
    __tablename__ = 'LostAndFound'
    id = db.Column(db.Integer,nullable=False,primary_key=True,autoincrement=True)
    user_id = db.Column(db.String(32),nullable=False,index=True)
    lost_or_found = db.Column(db.String(5),nullable=False)
    article = db.Column(db.String(15),nullable=False)
    send_name = db.Column(db.String(10), nullable=False)
    receive_name = db.Column(db.String(10), nullable=True)
    content = db.Column(db.String(500),nullable=False)
    is_show_head = db.Column(db.Integer,server_default=text('False'),nullable=False)
    create_time = db.Column(db.DateTime, server_default=func.now())
    modify_time = db.Column(db.DateTime, server_default=func.now())
    deleted = db.Column(db.Integer, server_default=text('False'),nullable=False)
    state = db.Column(db.Integer, server_default=text('False'),nullable=False)

    def __init__(self,user_id,lost_or_found,article,send_name,content,is_show_head):
        self.user_id = user_id
        self.lost_or_found = lost_or_found
        self.article = article
        self.send_name = send_name
        self.content = content
        self.is_show_head = is_show_head

    @property
    def create_time_str(self):
        now_utc = time.mktime(datetime.datetime.now().timetuple())
        create_time_utc = time.mktime(self.create_time.timetuple())
        minute = int((now_utc - create_time_utc) / 60)
        if minute <= 60:
            return '%d分钟前' % (minute / 60)
        elif minute <= 60 * 24:
            return u'%d小时前' % (minute / 60)
        elif minute <= 60 * 24 * 2:
            return '昨天'
        elif minute <= 60 * 24 * 30:
            return '%d天前' % (minute / 60 /24 )
        else:
            return self.create_time.strtime("%Y-%m-%d")

    @classmethod
    def get_unread_num(cls):
        '''未审核数量'''
        num = cls.query.filter_by(state=LostAndFoundState.UNCHECK).count()
        return num

    @classmethod
    def get_today_send_num_by_user_id(cls,user_id):
        '''检查今天发送失物招领信息的次数'''
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        num = cls.query.filter_by(user_id=user_id,state=LostAndFoundState.NORMAL).filter(
            cls.create_time >= today
        ).count()
        return num

    @classmethod
    def get_info_by_id(cls,id):
        '''根据id读取表白墙信息'''
        info = cls.query.filter_by(id=id).first()
        return info

    @classmethod
    def get_today_info_by_send_name(cls,send_name):
        '''读取当天发送者'''
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        info = cls.query.filter_by(send_name=send_name) \
            .filter(cls.state >= LostAndFoundState.NORMAL,
                    cls.create_time.between(now + datetime.timedelta(hours=-24), now)) \
            .first()
        return info

    @classmethod
    def get_page(cls, state, num, page):
        """分页读取失物招领信息"""
        info = cls.query.filter_by(state=state).order_by(
            cls.id.desc()).paginate(page, num, False)
        return info

    @classmethod
    def get_main_list(cls, state, max_show, like_sort=True):
        """读取失物招领信息"""
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        # 读取今天的数据
        info = cls.query \
            .filter(cls.state >= state,
                    cls.create_time.between(now + datetime.timedelta(hours=-24), now))
        if info.count() < max_show:
            # 如果今天的数据小于最多最大展示数量，则按时间排序显示全部
            info = cls.query.filter(cls.state >= state)
        if like_sort:
            info = info.order_by(cls.like_num.desc(), cls.id.desc())
        else:
            # 最多显示15天前数据
            info = info.filter(cls.create_time.between(now + datetime.timedelta(days=-15), now))\
                .order_by(cls.state.desc(), cls.id.desc())
        info = info.limit(max_show)
        return info.all()

    @classmethod
    def set_state(cls, id, state):
        """设置发布状态"""
        info = cls.query.filter_by(id=id).first()
        if info:
            info.state = state if state >= -1 else -1
            info.modify_time = datetime.datetime.now()
            db.session.commit()



class Admin(db.Model):
    user_id = db.Column(db.String(32),nullable=False,primary_key=True,index=True)
    admin_name = db.Column(db.String(10), nullable=False)

    def __init__(self,user_id,admin_name):
        self.user_id = user_id
        self.admin_name = admin_name