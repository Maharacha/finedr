from charms.reactive import when, when_not, set_flag
from charmhelpers.core.hookenv import resource_get, log
import tarfile
import subprocess
import os

@when_not('finedr-docker.installed')
def install_finedr_docker():
  # Do your setup here.
  #
  # If your charm has other dependencies before it can install,
  # add those as @when() clauses above., or as additional @when()
  # decorated handlers below
  #
  # See the following for information about reactive charms:
  #
  #  * https://jujucharms.com/docs/devel/developer-getting-started
  #  * https://github.com/juju-solutions/layer-basic#overview
  #
  repo_tar = resource_get('finedr')
  if os.stat(repo_tar).st_size > 0:
      tar = tarfile.open(repo_tar)
      tar.extractall(path=str('/finedr'))
      tar.close()
      log("Repo Installed")
  else:
      log("Repo *NOT* Installed")

  set_flag('finedr-docker.installed')

@when('finedr-docker.installed')
def run_finedr_docker():
  orig_pwd = os.getcwd()
  os.chdir('/finedr')
  subprocess.run(['docker-compose', 'up', '-d'])
  os.chdir(orig_pwd)
