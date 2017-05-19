import os

lines = open('data').read()
with open('data','w') as file:
    file.write( 'Name             2D atoms  3D atoms       2D Energy          3D Energy    Energy of Formation\n')

energy2= '    I   '
energy3= '    I   '
for direct in os.listdir('sortedcompounds_2D'):
     
    if os.path.isdir('sortedcompounds_2D/'+direct):
        
        for comp in os.listdir('sortedcompounds_2D/'+direct):
            if os.path.isdir('sortedcompounds_2D/'+direct+'/'+comp):
                x=0
                lines2 = open('sortedcompounds_2D/'+direct+'/'+comp+'/POSCAR').readlines()
                atoms2 = lines2[6].split()
                atoms2 = int(atoms2[0]) +int(atoms2[1])
                elines2 = open('sortedcompounds_2D/'+direct+'/'+comp+'/OUTCAR').readlines()
                for eline2 in elines2:
                    el2=eline2.strip()
                    if el2.startswith("free  energy   TOTEN"):
                          
                        e2 = el2.split()
                        
                        energy2 = float(e2[4])
                         
                    if  el2.startswith("reached required accuracy"):
                        
                        x=1
                if x==0:
                    energy2='     I   '
                y=0
                lines3 = open('sortedcompounds_3D/'+direct+'/'+comp+'/POSCAR').readlines()
                atoms3 = lines3[6].split()
                atoms3 = int(atoms3[0]) +int(atoms3[1])
                elines3 = open('sortedcompounds_3D/'+direct+'/'+comp+'/OUTCAR').readlines()
                for eline3 in elines3:
                    el3=eline3.strip()
                    if el3.startswith("free  energy   TOTEN"):
                        e3 = el3.split()
                        energy3 = float(e3[4])
                    if el3.startswith("reached required accuracy"):
                       x=1
                if x==0:
                    energy3 = '    I   '

                try:
                    energy = str(energy2/atoms2 - energy3/atoms3)
                except: energy = "-"
                mid0= direct+comp[2:]+'            '
                mid= mid0[:15] +'     '+ (str(atoms2)+'     ')[:5]+'     '+ (str(atoms3)+'     ')[:5]+'     ' + (str(energy2)+'         ')[:16]+'     '+(str(energy3)+'         ')[:16]+'     '+str(energy)
                
                
                lines = open('data').read()
                with open('data','w') as file:
                    file.write(lines)
                    file.write(mid+'\n')
                 

