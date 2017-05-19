import os
os.system('cp --backup=numbered POSCAR POSCAR_');
os.system('cp CONTCAR POSCAR');
os.system('sbatch submit');
