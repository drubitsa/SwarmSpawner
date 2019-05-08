c = get_config()
# Configuration file for jupyterhub.
def hello_hook(spawner):
    spawner.log.info("Hook - Hello from pre_spawn_hook")
    return True


c.JupyterHub.spawner_class = 'jhub.SwarmSpawner'

c.JupyterHub.authenticator_class = 'jhubauthenticators.DummyAuthenticator'
c.DummyAuthenticator.password = 'password'

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.cleanup_servers = False

# First pulls can be really slow, so let's give it a big timeout
c.SwarmSpawner.start_timeout = 60 * 5

c.SwarmSpawner.jupyterhub_service_name = 'jupyterhub'
c.SwarmSpawner.networks = ["jupyterhub_default"]

c.SwarmSpawner.use_user_options = True

c.SwarmSpawner.container_spec = {
    # The command to run inside the service
    'env': {'JUPYTER_ENABLE_LAB': '1'}
}

c.SwarmSpawner.pre_spawn_hook = hello_hook

c.SwarmSpawner.dockerimages = [
    {'name': 'Base Notebook',
     'image': 'nielsbohr/base-notebook',
     'env': {'NB_USER': '{_service_owner}',
             'NB_UID': '{uid}',
             'HOME': '/home/{_service_owner}',
             'CHOWN_HOME': 'yes',
             'GRANT_SUDO': 'no'},
     'uid_gid': 'root',
     # Better to substitute mkdir with a /usr/local/bin/start-notebook.d
     # hook via jupyter/base-notebook
     'command': "/bin/bash -c 'mkdir -p /home/{_service_owner}; /usr/local/bin/start-notebook.sh'"
    }
]
