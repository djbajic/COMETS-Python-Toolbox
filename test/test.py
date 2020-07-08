#!/usr/bin/env python

import cobra
import cobra.test
import comets


m = cobra.test.create_test_model('textbook')
m = comets.model(m)
m.initial_pop = [1, 1, 1e-5]

lyt = comets.layout(m)

lyt.add_external_reaction('rxn1', ['akg_e', 'ac_e', 'h_e'],
                          [-1, 1, 1], K=1e-5)

lyt.add_external_reaction('rxn2', ['glu__L_e', 'fum_e', 'for_e'],
                          [-1, 1, 1], Kcat=1e-3, Km=1e-2)

lyt.write_layout('/home/djordje/Dropbox/projects/COMETS-Python-Toolbox/test')



##
m.add_light(['ACKr', .5, .9])
m.write_comets_model('/home/djordje/Dropbox/projects/COMETS-Python-Toolbox/test')
