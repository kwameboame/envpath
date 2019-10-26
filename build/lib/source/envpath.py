from pathlib import Path
import os
import subprocess
import argparse
import logging

# Configure logger
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Create global variables
env_path = Path.cwd()
localpath = os.getenv('LOCALAPPDATA')
joinpath = Path(localpath).joinpath('Envpath')
crtpath = joinpath.mkdir(parents=False, exist_ok=True)
crtpath = os.path.expandvars(r'%LOCALAPPDATA%\Envpath')
envnames = {}


def set_envpath(getenvname):
    '''This function saves the name and path of your active env. It creates a
    batch file that contains commands to activate the env and CD to the path
    when the env is called.'''

    # Set key-value pair of envname : path
    envnames[getenvname] = env_path
    # Save the path
    f = open(crtpath + "/{}.bat".format(getenvname), "w+")
    # Write commands to batch file
    f.write('''@echo off \ncmd /k "cd {} && workon {}"
            '''.format(env_path, list(envnames.keys())[0]))
    f.close()
    logging.info("Envpath '{}' saved".format(getenvname))


def run_batch(envname):
    '''This function activates the env that is called and runs the batch file
    saved by the set_envpath() function.'''

    envdirs = os.chdir(crtpath)
    file_list = os.listdir(envdirs)
    envname = envname + ".bat"

    logging.info("Running commands in {}".format(envname))

    if envname in file_list:
        filepath = os.path.abspath(envname)
        subprocess.call(filepath)
    else:
        logging.info("Sorry, env not saved. Run 'envpath save' to save it")


# Set up parser
def runnit():
    parser = argparse.ArgumentParser(description="Manage dev en paths")
    parser.add_argument('-s', '--save', metavar='',
                        help="Save environment name and path")
    parser.add_argument('-o', '--open', metavar='',
                        help="Activate saved environment and path")
    args = parser.parse_args()

    if args.save:
        set_envpath(args.save)
    elif args.open:
        run_batch(args.open)
    else:
        logging.info("\nNo options received!\nRun 'envpath -h' to see options")
