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
                os.chdir('{}/{}'.format(comp,sys.argv[1]))
                os.system('rm AECC* CHG* DOS* EIG* WAVE* XDAT*') #clears all the unnecessary files from the current directory
                os.chdir('../'+sys.argv[2])
                print GREEN+comp+NC
        except:
                pass 
