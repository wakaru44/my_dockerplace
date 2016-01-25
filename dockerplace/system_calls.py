
from os.path import join, isfile
import md5
from fabric.api import local, settings
from retricon import retricon

from helpers import is_there_makefile, parse_make


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
    if is_there_makefile(output):
        output = do_run(
            """cd {0};\
                    cat Makefile | grep "^[a-z]*:" | cut -d ":" -f 1""".format(
                makefile_base))
        actions = parse_make(output)
    else:
        actions = []

    return actions


def get_all_actions(docker_home):
    """
    get the list of all actions for all the containers
    """
    containers = get_containers(docker_home)
    services = []
    for container in containers:
        print("XXX: " + docker_home + "/" + container)
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
