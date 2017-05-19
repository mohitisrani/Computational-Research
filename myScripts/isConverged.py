import os
import sys
from mpinterfaces.utils import is_converged
RED='\033[0;31m'
LRED='\033[1;31m'
NC='\033[0m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'

for comp in os.listdir('.'):
    if os.path.isdir(comp):
        try:
            if is_converged('{}/{}'.format(comp,sys.argv[1])):
                print GREEN+comp+NC
            else:
                print LRED+comp+" - NOT converged"+NC;
        except:
                print CYAN+comp+" - NO such directry exists"+NC;
