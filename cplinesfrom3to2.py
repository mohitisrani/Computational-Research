#copies ISPIN and MAGMOM values from 3d to 2d from the INCAR files

import os


for direct in os.listdir('msortedcompounds_3D'):
     
    if os.path.isdir('msortedcompounds_3D/'+direct):
        
        for comp in os.listdir('msortedcompounds_3D/'+direct):
            if os.path.isdir('msortedcompounds_3D/'+direct+'/'+comp):
                
                lines3 = open('msortedcompounds_3D/'+direct+'/'+comp+'/INCAR').readlines()
                
                for line3 in lines3:
                    l3=line3.strip()
                    if l3.startswith("ISPIN"):
                        ISPIN=l3
                    if l3.startswith("MAGMOM"):
                        MAGMOM=l3
                        
            
                lines2 = open('msortedcompounds_2D/'+direct+'/'+comp+'/INCAR').read()
                with open('msortedcompounds_2D/'+direct+'/'+comp+'/INCAR','w') as file:
                    file.write(lines2+'\n')
                    file.write(ISPIN+'\n'+MAGMOM)                        

