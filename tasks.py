from invoke import task
import subprocess


def make(c, target, talk):
    # check pwd
    ret_pwd = subprocess.check_output(["pwd"]).decode('ascii')
    ret_git = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('ascii')
    assert ret_pwd == ret_git

    # check talk
    assert '/' not in talk[-1]

    cmd = "make -C talks/%s -f ../../tools/Makefile %s" % (talk, target)
    c.run(cmd)


@task
def list(c):
    print("Available talks:")
    ret = subprocess.check_output(["ls", "talks/"]).decode('ascii')
    for talk in ret.split("\n"):
        talk = talk.strip()
        if talk:
            print("* %s" % talk)


@task
def build(c, talk):
    make(c, "build", talk)


@task
def build_handout(c, talk):
    make(c, "build-handout", talk)


@task
def clean(c, talk):
    make(c, "clean", talk)


@task
def open(c, talk):
    make(c, "open", talk)
