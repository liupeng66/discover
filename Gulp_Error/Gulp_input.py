#!/usr/bin/python2
#Change the format of crystal structure
#python Str_Format.py infile outfile
try:
    from pymatgen.io.vasp.inputs           import Poscar
    from pymatgen                          import Structure
    from pymatgen.command_line.gulp_caller import GulpIO
except:
    print 'You should install pymatgen first.'
    exit(0)

import sys
from monty.io import zopen


if __name__ == '__main__':
    Gulp = GulpIO()

    #change the Structure
    #Cry_Str = Structure.from_file("POSCAR")
    #gulpinput = Gulp.structure_lines(structure = Cry_Str)
    #with open('gulpinput','w') as f:
        #f.write(gulpinput)
    #exit(0)
    
    #output the energy
    with zopen('log', "rt") as f:
        contents = f.read()
    energy = Gulp.get_energy(contents)
    print energy

    #output the relaxed structure
    with zopen('log', "rt") as f:
        contents = f.read()
    Opt_Str = Gulp.get_relaxed_structure(contents)
    Vasp_Str = Poscar(Opt_Str)
    Vasp_Str.write_file('out.vasp')
