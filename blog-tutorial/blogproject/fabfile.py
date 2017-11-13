# -*- coding: utf-8 -*-
from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/waiwai948/sakura.git"

env.user = 'root'
env.password = '508371431@qq.com'

# 填写你自己的主机对应的域名
env.hosts = ['39.106.98.36']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/gsc/sites/gsce.cc/sakura/blog-tutorial/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
        cd /home/gsc/sites/gsce.cc/sakura/blog-tutorial/blogproject &&
        /home/gsc/sites/gsce.cc/env/bin/pip install -r requirement.txt &&
        /home/gsc/sites/gsce.cc/env/bin/python3 manage.py collectstatic --noinput &&
        /home/gsc/sites/gsce.cc/env/bin/python3 manage.py migrate
        """)
    sudo('supervisorctl -c /etc/supervisor/supervisord.conf restart myblog')
    sudo('service nginx reload')
