#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-20"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["IC3392"] =  [ 113121, 113123, 113125, 113470, 113472, 113474, 113476,
                  124133, 124135,]           # dec 1

on["NGC3338"] = [ 124466,                             # dec 3
                  124744, 124746, 124748, 124750,     # dec 5
                  124860, 124862, 124864, 124868,     # dec 10
                  126792, ]


on["NGC3430"] = [ 123376, 123378, 123380,    # nov 26
                  123549,                    # nov 27
                  124121, 124123,            # dec 1
                  124456, 124458,            # dec 3
	          126802, 
                  126928, 126930,]           # feb 9

on["NGC3486"] = [ 126936, 126938, 126940, 126946, 126948,       # feb 9
                  127068, 127070, 127072, 127080,               # feb 10
                  127911, 127913,]

on["NGC4189"] = \
 [ 113113, 113115, 113117, 113462, 113464, 113466, 115034, 115036, 115038, 
   115040, 115044, 115046, 115048, 116485, 116487,]

on["NGC4536"] = \
 [ 127958, 127960, 127962, 128247, 128249, 128637,]

on["NGC4536_SB0"] = \
 [ 129493, 131319, 131340, 131669, ]

on["NGC4536_SB1"] = \
 [ 129495, 131321, 131373, 131671, ]

on["NGC5012"] = \
 [ 124476, 124478,
   124758, 124760, 124762,
   124872, 124874, 124876, 124878,]

on["NGC5033"] = \
 [ 132880, 132882, 132890, 133279, 133281, 133287, 133289, 133291,]

on["NGC5033_SB0"] = \
 [ 131329, 131381, 131717, 132095, 132103, 132136, 132200,]

on["NGC5033_SB1"] = \
 [ 131331, 131383, 131721, 132097, 132105, 132138, 132202,]

on["NGC5347"] = \
 [ 112756, 112758, 112760, 112762, 112764, 112770, 112772, 112774, 112776, 
   112778, 112871, 112958, 112960,]

on["NGC5899"] = \
 [ 114780, 114782, 114784, 114788, 114790, 114792, 114798, 116491, 116493, 
   116495, 116497, 116499, 116501,]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["IC3392"]  = "pix_list=-13,14,15  dv=150 dw=250 qagrade=3"
pars1["NGC3338"] = "pix_list=-13,14,15  dv=250 dw=250 qagrade=3"
pars1["NGC3430"] = "pix_list=-13,14,15  dv=250 dw=250 qagrade=3"
pars1["NGC3486"] = "pix_list=-13,14,15  dv=250 dw=250 qagrade=3"
pars1["NGC4189"] = "pix_list=-13,14,15  dv=150 dw=250 qagrade=3"
pars1["NGC4536"] = "pix_list=-13,14,15  dv=250 dw=250"
pars1["NGC4536_SB0"] = "dv=250 dw=250"
pars1["NGC4536_SB1"] = "dv=250 dw=250"
pars1["NGC5012"] = "pix_list=-13,14,15  dv=300 dw=300 qagrade=3"
pars1["NGC5033"]     = "dv=300 dw=300"
pars1["NGC5033_SB0"] = "dv=300 dw=300"
pars1["NGC5033_SB1"] = "dv=300 dw=300"
pars1["NGC5347"] = "pix_list=-13,14,15  dv=150 dw=250 vlsr=2400 qagrade=3"
pars1["NGC5899"] = "pix_list=-13,14,15  dv=350 dw=400 vlsr=2650 qagrade=3"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["IC3392"]  = "bank=0 pix_list=-13"
pars2["NGC3338"] = "bank=0 pix_list=-13"
pars2["NGC3430"] = "bank=0 pix_list=-13"
pars2["NGC3486"] = "bank=0 pix_list=-13"
pars2["NGC4189"] = "bank=0 pix_list=-13"
pars2["NGC4536"] = "bank=0 pix_list=-13"
pars2["NGC4536_SB0"] = "bank=0 pix_list=-13"
pars2["NGC4536_SB1"] = "bank=0 pix_list=-13"
pars2["NGC5012"] = "bank=0 pix_list=-13"
pars2["NGC5033"]     = "bank=0 pix_list=-13"
pars2["NGC5033_SB0"] = "bank=0 pix_list=-13"
pars2["NGC5033_SB1"] = "bank=0 pix_list=-13"
pars2["NGC5347"] = "bank=0 pix_list=-13"
pars2["NGC5899"] = "bank=0 pix_list=-13"


#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["IC3392"]  = "bank=1 pix_list=-13,14,15"
pars3["NGC3338"] = "bank=1 pix_list=-13,14,15"
pars3["NGC3430"] = "bank=1 pix_list=-13,14,15"
pars3["NGC3486"] = "bank=1 pix_list=-13,14,15"
pars3["NGC4189"] = "bank=1 pix_list=-13,14,15"
pars3["NGC4536"] = "bank=1 pix_list=-13,14,15"
pars3["NGC5012"] = "bank=1 pix_list=-13,14,15"
pars3["NGC5033"] = "bank=1 pix_list=-13,14,15"
pars3["NGC5347"] = "bank=1 pix_list=-13,14,15"
pars3["NGC5899"] = "bank=1 pix_list=-13,14,15"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
