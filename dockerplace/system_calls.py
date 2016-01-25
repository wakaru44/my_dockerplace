
from os.path import join, isfile
import md5
from fabric.api import local, settings
from retricon import retricon

from helpers import is_there_makefile, parse_make, sanitize


def do_run(command):
    """simplify command running"""
    with settings(warn_only=True):
        return local(command, capture=True)


def get_imageid(something):
    """
    create an identicon picture out of a string
    """
    # just in case, keep the locations in a dir
    loc_loc = get_containers(".")
    location = {"web": "/static/cache", "local": "dockerplace/static/cache"}
    # instead of the string, we use a hash to avoid weird characters
    hashname = md5.new(something).hexdigest()
    # create the identicon
    print hashname
    # save in the local folder under a hashname
    filename = hashname + ".png"
    savepath = join(location["local"], filename)
    if not isfile(savepath):
        # only create if it doesn't exist already
        img = retricon(str(hashname))
        img.save(savepath, "PNG")
    return join(location["web"], filename)


def get_container_actions(makefile_base):
    """
    get the available actions from the makefile in a given folder
    """
    output = do_run("ls {0}".format(makefile_base))
    if output.find("Makefile") >0:
    # if is_there_makefile(output):  # this is a dependency nightmare to test
        output = do_run(
            """cd {0};\
                    cat Makefile | grep "^[a-z]*:" | cut -d ":" -f 1""".format(
                makefile_base))
        # actions = parse_make(output)  # for now, I will not try to parse output smart
        actions = output.split("\n")
    else:
        actions = ["None"]

    return actions


def get_all_actions(docker_home):
    """
    get the list of all actions for all the containers
    """
    containers = get_containers(docker_home)
    services = []
    for container in containers:
        actions = get_container_actions(join(docker_home, container))
        services.append(
            {
                "name": container,
                "actions": actions,
                "image": get_imageid(container)
            }
            )

    return services


def get_containers(docker_home):
    """
    obtain the list of available folders in a given path.
    we assume this is a list of the available containers
    """
    output = do_run("ls {0}".format(docker_home))
    result = output.split()
    return result


def run_make_action(docker_home, service, action):
    """
    go and run the make tasks on the folder of the container.
    docker_home is needed while we find a better way of retrieving it,
    service is the name of the folder,
    action is the task to be run.
    """
    service = sanitize(service)
    action = sanitize(action)
    # seems obvious, is here for refactoring purposes
    docker_home = docker_home
    base_dir = join(docker_home, service)
    output = do_run("cd {0}; make {1}".format(base_dir, action))
    return output
