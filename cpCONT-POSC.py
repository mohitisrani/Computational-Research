
#copy CONTCAR to POSCAR
import os




for direct in os.listdir('.'):
    if os.path.isdir(direct):
        for comp in os.listdir(direct):
            if os.path.isdir(direct+'/'+comp):
                
                lines = open(direct+'/'+comp+'/CONTCAR').readlines()
                
                with open(direct+'/'+comp+'/POSCAR','w') as file:
                    for line in lines:
                        file.write(line)
                    
            else:continue
    else:continue

      
