from docopt import docopt
from docopt import DocoptExit
import sys
import subprocess

specification = sys.argv[1]
command_arguments = sys.argv[2]

try:
    arguments = docopt(specification, argv=command_arguments.split(), help=False, options_first=False)
    subprocess.run(f'echo ::set-output name=arguments::{arguments}'.split())
    subprocess.run("echo ::set-output name=valid::true".split())
except DocoptExit:
    subprocess.run("echo ::set-output name=valid::false".split())
