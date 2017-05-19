
#resubmit files if they did not fail but also did not complete, should be placed inside sortedcompounds 2d or 3d
#change 2D and 3D respectively
import os
import time



for direct in os.listdir('.'):
    if os.path.isdir(direct):
        for comp in os.listdir(direct):
            x=0
            y=0
            if os.path.isdir(direct+'/'+comp):
            
                elines = open(direct+'/'+comp+'/OUTCAR').readlines()
                for eline in elines:
                    el=eline.strip()
                    if el.startswith("POTLOK:  cpu time"):x=1
                    if el.startswith("reached required accuracy"):y=2                
                if x==1:                     
                    if y==0: 
                        print direct+" "+comp
                        os.chdir('/ufrc/hennig/misrani/sortedcompounds_2D/'+direct+'/'+comp)                
                        os.system('sbatch submit')
                        time.sleep(1)
                        os.chdir('../../')
            else:continue
    else:continue

