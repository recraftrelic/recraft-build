import subprocess


def create_app(app_name, origin, port=3000):
    if app_name is None or origin is None :
        return

    subprocess.call(['bash', './scripts/create_react_app.sh', app_name])
    # subprocess.call(['bash', './scripts/create_domain_config.sh', app_name, port])
    subprocess.call(['bash', './scripts/create_docker_compose_config.sh', app_name, port])
    subprocess.call(['bash', './scripts/push.sh', app_name, origin])
