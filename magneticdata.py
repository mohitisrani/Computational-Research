#prints last line of oszicar of all compounds in a magdata file
import os

with open('magdata','w') as file:
                    file.write('Magnetic data \n')


for direct in os.listdir('.'):
    
    if os.path.isdir(direct):
        
        for comp in os.listdir(direct):
            if os.path.isdir(direct+'/'+comp):
                lines = open(direct+'/'+comp+'/OSZICAR').readlines()
                for a in lines:
                    b=a
                
                lines = open('magdata').read()
                with open('magdata','w') as file:
                    file.write(lines)
                    file.write(direct+ ' ' +comp+ ' '+ b+'\n')


