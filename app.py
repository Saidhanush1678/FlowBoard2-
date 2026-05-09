from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Manager Created Users

team_leaders = [
    {
        "username": "rahul",
        "password": "123"
    }
]

team_members = [
    {
        "username": "akhil",
        "password": "123"
    }
]

# Projects

projects = [
    {
        "name": "AI Dashboard",
        "leader": "rahul",
        "status": "In Progress"
    }
]

# Tasks

tasks = [
    {
        "project": "AI Dashboard",
        "task": "Frontend UI",
        "member": "akhil",
        "status": "Pending"
    }
]

# ---------------- HOME ----------------

@app.route('/')
def home():
    return render_template('index.html')

# ---------------- LOGIN ----------------

@app.route('/manager_login')
def manager_login():
    return render_template('manager_login.html')

@app.route('/leader_login')
def leader_login():
    return render_template('leader_login.html')

@app.route('/member_login')
def member_login():
    return render_template('member_login.html')

# ---------------- DASHBOARDS ----------------

@app.route('/manager_dashboard')
def manager_dashboard():
    return render_template(
        'manager_dashboard.html',
        projects=projects,
        tasks=tasks
    )

@app.route('/leader_dashboard/<leader>')
def leader_dashboard(leader):

    leader_projects = []

    for p in projects:
        if p["leader"] == leader:
            leader_projects.append(p)

    return render_template(
        'leader_dashboard.html',
        leader=leader,
        projects=leader_projects,
        tasks=tasks
    )

@app.route('/member_dashboard/<member>')
def member_dashboard(member):

    member_tasks = []

    for t in tasks:
        if t["member"] == member:
            member_tasks.append(t)

    return render_template(
        'member_dashboard.html',
        member=member,
        tasks=member_tasks
    )

# ---------------- CREATE USERS ----------------

@app.route('/create_user')
def create_user():
    return render_template('create_user.html')

# ---------------- CREATE PROJECT ----------------

@app.route('/create_project')
def create_project():
    return render_template('create_project.html')

# ---------------- FILE UPLOAD ----------------

@app.route('/upload_code')
def upload_code():
    return render_template('upload_code.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    if file:

        path = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        file.save(path)

    return "Code Uploaded Successfully"

if __name__ == '__main__':
    app.run(debug=True)