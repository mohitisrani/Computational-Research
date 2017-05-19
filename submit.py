
import os
import time



for direct in os.listdir('.'):
    if os.path.isdir(direct):
        for comp in os.listdir(direct):
            if os.path.isdir(direct+'/'+comp):
                
                os.chdir('/ufrc/hennig/misrani/trial/'+direct+'/'+comp)
                
                os.system('sbatch submit')
                time.sleep(1)
                os.chdir('../../')
            else:continue
    else:continue
