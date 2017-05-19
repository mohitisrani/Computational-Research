from pymatgen.core.structure import Structure
from mpinterfaces.utils import add_vacuum_padding

struct_2d = Structure.from_file('POSCAR')
new_struct = add_vacuum_padding(struct_2d, 20)
new_struct.to(filename='POSCAR', fmt='poscar')

