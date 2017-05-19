from pymatgen.io.vasp.outputs import Vasprun

try:
    if Vasprun('vasprun.xml').converged:
        print '\033[92m'+'Converged'+'\033[0m'
    else:
        print '\033[93m'+'Not Converged'+'\033[0m'
except:
    print '\033[0;33m'+'Not Converged_NV'+'\033[0m'


#class bcolors:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#
#To use code like this, you can do something like
#
#print bcolors.WARNING + "Warning: No active frommets remain. Continue?" 
#      + bcolors.ENDC
