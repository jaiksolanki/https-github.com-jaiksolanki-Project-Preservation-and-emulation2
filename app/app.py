# from flask import Flask, flash, redirect, render_template, request, session, abort, url_for,json, jsonify, Response
# from flask_cors import CORS
# from flaskext.mysql import MySQL
# import re
# import git
# import os
# import sys
# import shutil
# import docker
# import socket
# mysql = MySQL()
# app = Flask(__name__)
# CORS(app)
# app.secret_key = os.urandom(12)
# app.config['MYSQL_DATABASE_USER'] = 'beproject'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Beproject'
# app.config['MYSQL_DATABASE_DB'] = 'dockengine'
# app.config['MYSQL_DATABASE_HOST'] = 'dockengine.cxd6jyo8ikqn.us-east-1.rds.amazonaws.com'
# mysql.init_app(app)
# #redis = Redis(host='redis', port=6379)

# client = docker.from_env()

# @app.route("/")
# def slogin():
#     if 'user' in session :
#         return redirect(url_for("sdashboard"))
#     else:
#         return render_template('slogin.html')


# @app.route("/tlogin")
# def tlogin():
#     if 'user' in session :
#         return redirect(url_for("tdashboard"))
#     else:
#         return render_template('tlogin.html')

# @app.route("/form")
# def form():
#     return render_template("form.html",username=session.get('user'))

# @app.route("/blackbook")
# def blackbook():
#     return render_template("blackbook.html",username=session.get('user'))

# @app.route("/addbb", methods=['GET', 'POST'])
# def addbb():
#     pid=str(request.form['pid'])
#     bb=str(request.form['bburl'])
#     print(pid)
#     print(bb)
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("UPDATE Project set blackbook='"+bb+"' where Pid='"+pid+"'")
#     return render_template("blackbook.html",username=session.get('user'))

# @app.route('/build', methods=['GET', 'POST'])
# def build_image():
#     github_url=str(request.form['githuburl'])
#     user=session.get('user')
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     projcount=cursor.execute("SELECT COUNT(*) from Project where Gid='" + user + "'")
#     projectID=user+"_"+str(projcount+1)
#     url=github_url
#     basename=os.path.basename(url)
#     filename=basename.split(".")
#     pathuser=str(filename[0])
#     if not os.path.exists("temp/"+pathuser):
#         git.Git("temp/").clone(github_url)
#     else:
#         try:
#             shutil.rmtree("temp/"+pathuser)
#         except OSError, e:
#             print ("Error: %s - %s." % (e.filename,e.strerror))
#         git.Git("temp/").clone(github_url)
#     client.images.build(path='temp/'+pathuser,tag='127.0.0.1:4000/'+pathuser)
#     for line in client.images.push('127.0.0.1:4000/'+pathuser,stream=True):
#         print(line)
#     imgurl='127.0.0.1:4000/'+pathuser
#     cursor.execute("INSERT INTO Project (Gid,Pid,ProjectName,Gitlink) VALUES (%s,%s,%s,%s)",(user,projectID,pathuser,github_url))
#     cursor.execute("INSERT INTO Image (Gid,Pid,Imglink) VALUES (%s,%s,%s)",(user,projectID,imgurl))
#     conn.commit()
#     return redirect(url_for("sdashboard"))

# @app.route('/projects', methods=['GET', 'POST'])
# def project():
#     print(session.get('user'))
#     if 'user' in session:
#         user = session.get('user')
#     else:
#         return redirect(url_for("slogin"))
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT Pid, ProjectName, Pstatus, ip from Project where Gid='" + user + "'")
#     row_headers=[x[0] for x in cursor.description] #this will extract row headers
#     rv = cursor.fetchall()
#     json_data=[]
#     for result in rv:
#         json_data.append(dict(zip(row_headers,result)))
#     return json.dumps(json_data)

# # @app.route("/run/", methods=['POST'])
# # def run_container():
# #     global container
# #     container= client.containers.run('test',detach=True)
# #     image = container.commit("test")
# #     return render_template('index.html')

# # @app.route("/save/", methods=['POST'])
# # def save_image():
# #     image = client.images.push(repository='',tag='')
# #     return render_template('dashboard.html')

# # @app.route("/stop/", methods=['POST'])
# # def stop_container():
# #     container.stop()
# #     return render_template('dashboard.html')

# # @app.route("/delete/", methods=['POST'])
# # def delete_container():
# #     container.remove()
# #     return render_template('dashboard.html')

# # @app.route("/start/", methods=['POST'])
# # def start_container():
# #     container.start()
# #     return render_template('dashboard.html')

# @app.route("/loginTeacher", methods=["POST"])
# def loginTeacher():
#     session.permanent = True
#     print("in")
#     if request.method=='POST':
#         user = str(request.form['username'])
#         pass1= str(request.form['password'])
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("SELECT Pass from TLogin where Tid='" + user+ "'")
#         results=cursor.fetchall()
#             # for row in results:
#             #     pass2=row[0]
#         if pass1==results[0][0]:
#             session['user']=user
#             print('hi')
#             print(session['user'])
#             return redirect(url_for("tdashboard"))
#     return redirect(url_for("tlogin"))

# @app.route("/loginStudent", methods=["POST"])
# def loginStudent():
#     session.permanent = True
#     print("in")
#     if request.method=='POST':
#         user = str(request.form['username'])
#         pass1= str(request.form['password'])
#         conn = mysql.connect()
#         cursor = conn.cursor()
#         cursor.execute("SELECT Pass from SLogin where Gid='" + user+ "'")
#         results=cursor.fetchall()
#             # for row in results:
#             #     pass2=row[0]
#         if pass1==results[0][0]:
#             session['user']=user
#             print('hi')
#             print(session['user'])
#             return redirect(url_for("sdashboard"))
#     return redirect(url_for("slogin"))

# @app.route("/rmcontainer")
# def rmcontainer():
#     gid=session.get('user')
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT Imglink from Image where Pid in (Select Pid From Project Where Pstatus='Running' and Gid='"+gid+"')" )
#     results=cursor.fetchone()
#     imglink=results[0]
#     basename=os.path.basename(imglink)
#     for container in client.containers.list():
#         if container.name==basename:
#             container.stop()
#             container.remove(v=True)
#     status="Stopped"
#     ip="-"
#     cursor.execute ("UPDATE Project SET ip=%s, Pstatus=%s WHERE pid=%s", (ip,status,pid))
#     conn.commit()

# @app.route("/slogout")
# def slogout():
#     session.pop('user',None)
#     return redirect(url_for("slogin"))

# @app.route("/tlogout")
# def tlogout():
#     session.pop('user',None)
#     return redirect(url_for("tlogin"))

# # @app.route("/tlogout")
# # def tdashboard():
# #     session.pop()
# #     return render_template("tlogin.html")

# @app.route("/sdashboard")
# def sdashboard():
#     # user=session['user']
#     return render_template("sdashboard.html")

# @app.route("/tdashboard")
# def tdashboard():
#     return render_template("tdashboard.html")

# # @app.route('/test',methods=["POST"])
# # def test():
# #     conn = mysql.connect()
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT ProjectName from Project where Gid='G2018_1'" )
# #     results=cursor.fetchall()
# #     for row in results:
# #         pname=row[0]
# #     return render_template("test.html",ProjectName=pname)

# @app.route('/start',methods=['GET', 'POST'])
# def start():
#     pid = str(request.form['pid'])
#     print(pid)
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT Imglink from Image where Pid='" +pid+ "'" )
#     results=cursor.fetchone()
#     imglink=results[0]
#     basename=os.path.basename(imglink)
#     client.images.pull(imglink)
#     port=get_free_tcp_port()
#     client.containers.run(imglink,detach=True,name=basename,ports={'80/tcp': port})
#     ip="http://127.0.0.1:"+str(port)
#     print(ip)
#     status="Running"
#     query = """ UPDATE Project
#                 SET ip = %s,
#                 Pstatus = %s
#                 WHERE Pid = %s """
#     cursor.execute (query, (ip,status,pid))
#     conn.commit()
#     return redirect(url_for("sdashboard"))

# @app.route('/stop',methods=['GET', 'POST'])
# def stop():
#     pid = str(request.form['pid'])
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT Imglink from Image where Pid='" +pid+ "'" )
#     results=cursor.fetchone()
#     imglink=results[0]
#     basename=os.path.basename(imglink)
#     for container in client.containers.list():
#         if container.name==basename:
#             container.stop()
#             container.remove(v=True)
#     status="Stopped"
#     ip="-"
#     cursor.execute ("UPDATE Project SET ip=%s, Pstatus=%s WHERE pid=%s", (ip,status,pid))
#     conn.commit()
#     return redirect(url_for("sdashboard"))

# @app.route('/tdisplay1')
# def tdisplay1():

#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT Pid from Project where Gid='2018'")
#     results=cursor.fetchall()

#     for row in results:
#         Pid=row[0]

#     cursor.execute("SELECT ProjectName from Project where Pid='"+ Pid +"'")
#     results=cursor.fetchall()
#     for row in results:
#         pname=row[0]
#     cursor.execute("SELECT Imglink from Image where Pid='"+ Pid +"'")
#     results=cursor.fetchone()
#     imglink=results[0]
#     basename=os.path.basename(imglink)
#     client.images.pull(imglink)
#     client.containers.run(imglink,detach=True,name=basename,ports={'80/tcp': 32768})
#     ip="http://localhost:32768"

#     return render_template("tdisplay1.html",ProjectName=pname,IPadd=ip)

# @app.route('/tdisplay',methods=["GET","POST"])
# def tdisplay():
#     print(session.get('user'))
#     if 'user' in session:
#         user = session.get('user')
#     else:
#         return redirect(url_for("slogin"))
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     searchfield=session.get('searchfield')
#     if searchfield.isnumeric():
#         print("number hai detect hua")
#         cursor.execute("SELECT Pid, ProjectName, Pstatus, ip, blackbook from Groups NATURAL JOIN Project where Rollno=" + searchfield)
#     else :
#         cursor.execute("SELECT Pid, ProjectName, Pstatus, ip, blackbook from Project where Gid='" + searchfield + "'")
#     row_headers=[x[0] for x in cursor.description] #this will extract row headers
#     rv = cursor.fetchall()
#     json_data=[]
#     for result in rv:
#         json_data.append(dict(zip(row_headers,result)))
#     return json.dumps(json_data)
# # def tdisplay():
#     # Pid =  str(request.form['Pid'])
#     # conn = mysql.connect()
#     # cursor = conn.cursor()
#     # cursor.execute("SELECT ProjectName from Project where Pid='"+ Pid +"'")
#     # results=cursor.fetchall()
#     # for row in results:
#     #     pname=row[0]
#     # return render_template("tdisplay.html",ProjectName=pname)

# def get_free_tcp_port():
#     tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     tcp.bind(('', 0))
#     addr, port = tcp.getsockname()
#     tcp.close()
#     return port

# @app.route('/tstop')
# def tstop():
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     cursor.execute("SELECT Imglink from Image where Gid='G2018_1'" )
#     results=cursor.fetchone()
#     imglink=results[0]
#     basename=os.path.basename(imglink)
#     pname="test"
#     for container in client.containers.list():
#         if container.name==basename:
#             container.stop()
#     client.containers.prune()
#     return render_template("tdisplay.html",ProjectName=pname)

# @app.route('/tresult',methods=["POST"])
# def tresult():
#     session['searchfield']=str(request.form["searchfield"])
#     return render_template("tresult.html", username=session['user'])

# if __name__=='__main__':
#     app.run(debug=True,host='0.0.0.0')

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, json, jsonify, Response
from flask_cors import CORS
from flaskext.mysql import MySQL
from celery import Celery
from werkzeug.utils import secure_filename
import re
import git
import os
import sys
import shutil
import docker
import socket
mysql = MySQL()
app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(12)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['MYSQL_DATABASE_USER'] = 'beproject'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Beproject'
app.config['MYSQL_DATABASE_DB'] = 'dockengine'
app.config['MYSQL_DATABASE_HOST'] = 'dockengine.cxd6jyo8ikqn.us-east-1.rds.amazonaws.com'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
mysql.init_app(app)

client = docker.from_env()
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'doc', 'docx'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def slogin():
    if 'user' in session:
        return redirect(url_for("sdashboard"))
    else:
        return render_template('slogin.html')


@app.route("/tlogin")
def tlogin():
    if 'user' in session:
        return redirect(url_for("tdashboard"))
    else:
        return render_template('tlogin.html')


@app.route("/form")
def form():
    return render_template("form.html", username=session.get('user'))


@app.route("/blackbook")
def blackbook():
    return render_template("blackbook.html", username=session.get('user'))


@app.route("/addbb", methods=['POST'])
def addbb():
    conn = mysql.connect()
    cursor = conn.cursor()
    pid = str(request.form['pid'])
    gid = str(session.get('user'))
    rowcount = cursor.execute(
        'Select Pid from Project where Gid="'+gid+'" and Pid="'+pid+'"')
    if rowcount == 0:
        return render_template("blackbook.html", username=gid, errmsg="This project does not belong to you")
    if 'blackbook' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['blackbook']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        directory = os.path.join("blackbook/", gid, pid)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        else:
            shutil.rmtree(directory)
        directory = os.path.join(directory, filename)
        file.save(directory)
        cursor.execute("UPDATE Project set blackbook='" +
                       directory+"' where Pid='"+pid+"'")
        conn.commit()
        return render_template("blackbook.html", username=session.get('user'), errmsg="Uploaded Successfully")
    return render_template("blackbook.html", username=session.get('user'), errmsg="Wrong Filetype")


@app.route('/build', methods=['GET', 'POST'])
def build_image():
    github_url = str(request.form['githuburl'])
    container_port = str(request.form['port'])
    user = session.get('user')
    conn = mysql.connect()
    cursor = conn.cursor()
    projcount = cursor.execute(
        "SELECT PID from Project where Gid='" + user + "'")
    # print("projectcount"+str(cursor.rowcount))
    projectID = user+"_"+str(projcount+1)
    url = github_url
    basename = os.path.basename(url)
    filename = basename.split(".")
    pathuser = str(filename[0])
    asyn_build.delay(pathuser, github_url)
    # if not os.path.exists("temp/"+pathuser):
    #     git.Git("temp/").clone(github_url)
    # else:
    #     shutil.rmtree("temp/"+pathuser)
    #     git.Git("temp/").clone(github_url)
    # client.images.build(path='temp/'+pathuser, tag='127.0.0.1:4000/'+pathuser)
    # for line in client.images.push('127.0.0.1:4000/'+pathuser, stream=True):
    #     print(line)
    imgurl = '127.0.0.1:4000/'+pathuser
    cursor.execute("INSERT INTO Project (Gid,Pid,ProjectName,Gitlink,Port) VALUES (%s,%s,%s,%s,%s)",(user, projectID, pathuser, github_url,container_port))
    cursor.execute(
        "INSERT INTO Image (Gid,Pid,Imglink) VALUES (%s,%s,%s)", (user, projectID, imgurl))
    conn.commit()
    return redirect(url_for("sdashboard"))


@celery.task
def asyn_build(pathuser, github_url):
    if not os.path.exists("temp/"+pathuser):
        git.Git("temp/").clone(github_url)
    else:
        shutil.rmtree("temp/"+pathuser)
        git.Git("temp/").clone(github_url)
    client.images.build(path='temp/'+pathuser, tag='127.0.0.1:4000/'+pathuser)
    for line in client.images.push('127.0.0.1:4000/'+pathuser, stream=True):
        print(line)


@app.route('/update', methods=['GET', 'POST'])
def update():
    pid = str(request.form['pid'])
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Gitlink from Project where Pid='" + pid + "'")
    results = cursor.fetchone()
    github_url = u", ".join(results)
    url = github_url
    basename = os.path.basename(url)
    filename = basename.split(".")
    pathuser = str(filename[0])
    asyn_build.delay(pathuser, github_url)
    # if not os.path.exists("temp/"+pathuser):
    #     git.Git("temp/").clone(github_url)
    # else:
    #     shutil.rmtree("temp/"+pathuser)
    #     git.Git("temp/").clone(github_url)
    # client.images.build(path='temp/'+pathuser, tag='127.0.0.1:4000/'+pathuser)
    # for line in client.images.push('127.0.0.1:4000/'+pathuser, stream=True):
    #     print(line)
    return redirect(url_for("sdashboard"))


@app.route('/projects', methods=['GET', 'POST'])
def project():
    print(session.get('user'))
    if 'user' in session:
        user = session.get('user')
    else:
        return redirect(url_for("slogin"))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Pid, ProjectName, Pstatus, ip from Project where Gid='" + user + "'")
    # this will extract row headers
    row_headers = [x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)


@app.route("/rmcontainer")
def rmcontainer():
    gid = session.get('user')
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Imglink from Image where Pid in (Select Pid From Project Where Pstatus='Running' and Gid='"+gid+"')")
    results = cursor.fetchall()
    for row in results:
        imglink = row[0]
        basename = os.path.basename(imglink)
        for container in client.containers.list():
            if container.name == basename:
                container.stop()
                container.remove(v=True)
    status = "Stopped"
    ip = "-"
    cursor.execute(
        "UPDATE Project SET ip=%s, Pstatus=%s WHERE gid=%s", (ip, status, gid))
    conn.commit()


@app.route("/loginTeacher", methods=["POST"])
def loginTeacher():
    session.permanent = True
    print("in")
    if request.method == 'POST':
        user = str(request.form['username'])
        pass1 = str(request.form['password'])
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Pass from TLogin where Tid='" + user + "'")
        results = cursor.fetchall()
        if pass1 == results[0][0]:
            session['user'] = user
            print('hi')
            print(session['user'])
            return redirect(url_for("tdashboard"))
    return redirect(url_for("tlogin"))


@app.route("/loginStudent", methods=["POST"])
def loginStudent():
    session.permanent = True
    print("in")
    if request.method == 'POST':
        user = str(request.form['username'])
        pass1 = str(request.form['password'])
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT Pass from SLogin where Gid='" + user + "'")
        results = cursor.fetchall()
        if pass1 == results[0][0]:
            session['user'] = user
            print('hi')
            print(session['user'])
            return redirect(url_for("sdashboard"))
    return redirect(url_for("slogin"))


@app.route("/slogout")
def slogout():
    rmcontainer()
    session.pop('user', None)
    return redirect(url_for("slogin"))


@app.route("/tlogout")
def tlogout():
    session.pop('user', None)
    return redirect(url_for("tlogin"))


@app.route("/sdashboard")
def sdashboard():
    return render_template("sdashboard.html", username=session.get('user'))


@app.route("/tdashboard")
def tdashboard():
    return render_template("tdashboard.html")


@app.route('/start', methods=['GET', 'POST'])
def start():
    pid = str(request.form['pid'])
    print(pid)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Imglink from Image where Pid='" + pid + "'")
    results = cursor.fetchone()
    imglink = u", ".join(results)
    print(imglink)
    cursor.execute("SELECT Port from Project where Pid='" + pid + "'")
    results = cursor.fetchone()
    container_port = u", ".join(results)
    basename = os.path.basename(imglink)
    client.images.pull(imglink)
    port = get_free_tcp_port()
    client.containers.run(imglink, detach=True,
                          name=basename, ports={container_port+'/tcp': port})
    ip = "http://127.0.0.1:"+str(port)
    print(ip)
    status = "Running"
    query = """ UPDATE Project
                SET ip = %s,
                Pstatus = %s
                WHERE Pid = %s """
    cursor.execute(query, (ip, status, pid))
    conn.commit()
    return redirect(url_for("sdashboard"))


@app.route('/stop', methods=['GET', 'POST'])
def stop():
    pid = str(request.form['pid'])
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Imglink from Image where Pid='" + pid + "'")
    results = cursor.fetchone()
    imglink = results[0]
    basename = os.path.basename(imglink)
    for container in client.containers.list():
        if container.name == basename:
            container.stop()
            container.remove(v=True)
    status = "Stopped"
    ip = "-"
    cursor.execute(
        "UPDATE Project SET ip=%s, Pstatus=%s WHERE pid=%s", (ip, status, pid))
    conn.commit()
    return redirect(url_for("sdashboard"))


@app.route('/tstart', methods=['GET', 'POST'])
def tstart():
    pid = str(request.form['pid'])
    print(pid)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Imglink from Image where Pid='" + pid + "'")
    results = cursor.fetchone()
    imglink = u", ".join(results)
    print(imglink)
    cursor.execute("SELECT Port from Project where Pid='" + pid + "'")
    results = cursor.fetchone()
    container_port = u", ".join(results)
    basename = os.path.basename(imglink)
    client.images.pull(imglink)
    port = get_free_tcp_port()
    client.containers.run(imglink, detach=True,
                          name=basename, ports={container_port+'/tcp': port})
    ip = "http://127.0.0.1:"+str(port)
    print(ip)
    status = "Running"
    query = """ UPDATE Project
                SET ip = %s,
                Pstatus = %s
                WHERE Pid = %s """
    cursor.execute(query, (ip, status, pid))
    conn.commit()
    return redirect(url_for("tresult"))


@app.route('/tstop', methods=['GET', 'POST'])
def tstop():
    pid = str(request.form['pid'])
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT Imglink from Image where Pid='" + pid + "'")
    results = cursor.fetchone()
    imglink = results[0]
    basename = os.path.basename(imglink)
    for container in client.containers.list():
        if container.name == basename:
            container.stop()
            container.remove(v=True)
    status = "Stopped"
    ip = "-"
    cursor.execute(
        "UPDATE Project SET ip=%s, Pstatus=%s WHERE pid=%s", (ip, status, pid))
    conn.commit()
    return redirect(url_for("tresult"))


@app.route('/tdisplay', methods=["GET", "POST"])
def tdisplay():
    print(session.get('user'))
    if 'user' in session:
        user = session.get('user')
    else:
        return redirect(url_for("slogin"))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor1 = conn.cursor()
    searchfield = session.get('searchfield')
    if searchfield.isnumeric():
        print("number hai detect hua")
        cursor.execute(
            "SELECT Pid, ProjectName, Pstatus, ip, blackbook from Groups NATURAL JOIN Project where Rollno=" + searchfield)
        cursor1.execute("SELECT Gid,Sname,Rollno from Groups where Gid in (Select Gid from Groups where Rollno="+searchfield+")")
    else:
        cursor.execute(
            "SELECT Pid, ProjectName, Pstatus, ip, blackbook from Project where Gid='" + searchfield + "'")
        cursor1.execute(
            "SELECT Gid,Sname,Rollno from Groups where Gid='"+searchfield+"'")
    # this will extract row headers

    row_headers = [x[0] for x in cursor.description]
    rv = cursor.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    row_headers1 = [x[0] for x in cursor1.description]
    rv1 = cursor1.fetchall()
    for result in rv1:
        json_data.append(dict(zip(row_headers1, result)))

    print(json_data)

    return json.dumps(json_data)


def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


@app.route('/tresult', methods=["GET", "POST"])
def tresult():
    if request.method == "POST":
        session['searchfield'] = str(request.form["searchfield"])
    return render_template("tresult.html", username=session['user'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
