import subprocess


def create_app(app_name, origin):
    if app_name is None or origin is None :
        return

    subprocess.call(['bash', './scripts/create_react_app.sh', app_name])
    subprocess.call(['bash', './scripts/push.sh', app_name, origin])
