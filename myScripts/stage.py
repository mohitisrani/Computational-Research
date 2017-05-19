import os

RED='\033[0;31m'
NC='\033[0m'
YELLOW='\033[1;33m'
GREEN='\033[1;32m'
BLUE='\033[0;34m'
LBLUE='\033[1;34m'


toContinue='Y'
fileName='Y'
while (toContinue=='Y' or toContinue=='y'):
    jobid=raw_input("Job ID : ")
    os.system('cd \"$(dirname \"$(find /ufrc/hennig/misrani/ -name \"*'+jobid+'*\" | head -1)")";echo; echo -e \"${LBLUE}$(pwd)${NC}\";ls; echo; python /ufrc/hennig/misrani/stage/.scripts/isconverged.py;')
    while (fileName!='N' and fileName!='n' and fileName!='0'):
        fileName=raw_input("${YELLOW}Open File${NC}(enter 0 for none): ") 
        os.system('vim '+fileName)
    resubmit=raw_input("${GREEN}Resubmit the job${NC}(y  /Y(copy CONTCAR to POSCAR)  /N)")
    if resubmit=='Y':
        os.system('python /ufrc/hennig/misrani/stage/.scripts/resubmit.py')
    elif resubmit=='y':
        os.system('sbatch submit')
    toContinue=raw_input("${RED}Other jobs(y,n) : ${NC}")
   
