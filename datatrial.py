import os


for direct in os.listdir('.'):
    
    if os.path.isdir(direct):
        
        for comp in os.listdir(direct):
            if os.path.isdir(direct+'/'+comp):
                lines = open(direct+'/'+comp+'/POSCAR').readlines()
                atoms = lines[6].split()
                atoms = int(atoms[0]) +int(atoms[1])
                lines = open('data').read()
                with open('data','w') as file:
                    file.write(lines)
                    file.write(direct+ ' ' +comp+ ' '+ str(atoms)+'\n')

