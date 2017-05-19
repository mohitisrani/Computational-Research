# This will generate appropriate KPOINT file based on number of atoms

from decimal import Decimal

def makeKPOINTS(twoD, MeshType, desired_directory):
	#Input Variables
	MeshType = MeshType
	TwoDimensional = twoD
	input_POSCAR = desired_directory+'/POSCAR'
	output_KPOINTS = desired_directory+'/KPOINTS'
	Length = 50

	POSCAR = open(input_POSCAR, 'r')
	lines = POSCAR.readlines()
	scale = Decimal.from_float(float(lines[1].split()[0]))

	#Define original lattice vectors

	a1 = lines[2].split()
	a2 = lines[3].split()
	a3 = lines[4].split()

	a11 = scale*Decimal.from_float(float(a1[0]))
	a12 = scale*Decimal.from_float(float(a1[1]))
	a13 = scale*Decimal.from_float(float(a1[2]))

	a21 = scale*Decimal.from_float(float(a2[0]))
	a22 = scale*Decimal.from_float(float(a2[1]))
	a23 = scale*Decimal.from_float(float(a2[2]))

	a31 = scale*Decimal.from_float(float(a3[0]))
	a32 = scale*Decimal.from_float(float(a3[1]))
	a33 = scale*Decimal.from_float(float(a3[2]))

	#Calculate the determinant

	det = a11*(a22*a33-a23*a32)-a12*(a21*a33-a23*a31)+a13*(a21*a32-a22*a31)

	#Calculate reciprocal vectors

	b11 = (a22*a33-a23*a32)/det
	b12 = (a21*a33-a23*a31)/det
	b13 = (a21*a32-a22*a31)/det

	b21 = (a12*a33-a13*a32)/det
	b22 = (a11*a33-a13*a31)/det
	b23 = (a11*a32-a12*a31)/det

	b31 = (a12*a23-a13*a22)/det
	b32 = (a11*a23-a13*a21)/det
	b33 = (a11*a22-a12*a21)/det

	with open(output_KPOINTS, 'w') as file:
		kpoints_x = ''
		kpoints_y = ''
		kpoints_z = ''
		file.write('Automatic mesh\n')
		file.write( '0\n')
		l = Length 
		kpoints_x = round(float(l*Decimal.sqrt(b11*b11+b12*b12+b13*b13)))
		kpoints_y = round(float(l*Decimal.sqrt(b21*b21+b22*b22+b23*b23)))
		kpoints_z = round(float(l*Decimal.sqrt(b31*b31+b32*b32+b33*b33)))
		if TwoDimensional == True:
			kpoints_z =1
		file.write(MeshType + '\n')
		file.write(str(kpoints_x) + " " + str(kpoints_y) + " " + str(kpoints_z))
		print kpoints_x, kpoints_y, kpoints_z
if __name__ == '__main__':
	makeKPOINTS(False, 'Gamma','.') 
