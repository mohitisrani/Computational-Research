#edit the job name in 2D and 3D materials
import os
file_name='submit'
line_starts_with='#SBATCH --qos=hennig'
line_replaced_as='#SBATCH --qos=hennig-b'
lines = open(file_name).readlines()
with open(file_name,'w') as file:
    for line in lines:
        if line.startswith(line_starts_with):
            file.write(line_replaced_as+'\n')
        else:
            file.write(line)
                    

#PBS -N Al2Te3_mono_Al2Te3
#SBATCH -o job_%j.out   #Name output file
#SBATCH --mail-type=All   #What emails you want
#SBATCH --mail-user=mr.mohit.israni+HPG2@gmail.com
#SBATCH --nodes=1
#SBATCH --qos=hennig-b
#SBATCH --ntasks=32
#SBATCH --mem-per-cpu=2000mb   #Per processor memory request
#SBATCH -t 24:00:00   #Walltime in hh:mm:ss or d-hh:mm:ss

