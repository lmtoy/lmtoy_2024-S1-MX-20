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


on["NGC3430"] = [ 123376, 123378, 123380,    # nov 26
                  123549,                    # nov 27
                  124121, 124123,]           # dec 1


on["NGC4189"] = \
 [ 113113, 113115, 113117, 113462, 113464, 113466, 115034, 115036, 115038, 
   115040, 115044, 115046, 115048, 116485, 116487,]

on["NGC5347"] = \
 [ 112756, 112758, 112760, 112762, 112764, 112770, 112772, 112774, 112776, 
   112778, 112871, 112958, 112960,]

on["NGC5899"] = \
 [ 114780, 114782, 114784, 114788, 114790, 114792, 114798, 116491, 116493, 
   116495, 116497, 116499, 116501,]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["IC3392"]  = "pix_list=-13,14,15  dv=150 dw=250"
pars1["NGC3430"] = "pix_list=-13,14,15  dv=150 dw=250"
pars1["NGC4189"] = "pix_list=-13,14,15  dv=150 dw=250"
pars1["NGC5347"] = "pix_list=-13,14,15  dv=150 dw=250 vlsr=2400"
pars1["NGC5899"] = "pix_list=-13,14,15  dv=350 dw=400 vlsr=2650"


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["IC3392"]  = "bank=0 pix_list=-13"
pars2["NGC3430"] = "bank=0 pix_list=-13"
pars2["NGC4189"] = "bank=0 pix_list=-13"
pars2["NGC5347"] = "bank=0 pix_list=-13"
pars2["NGC5899"] = "bank=0 pix_list=-13"


#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["IC3392"]  = "bank=1 pix_list=-13,14,15"
pars3["NGC3430"] = "bank=1 pix_list=-13,14,15"
pars3["NGC4189"] = "bank=1 pix_list=-13,14,15"
pars3["NGC5347"] = "bank=1 pix_list=-13,14,15"
pars3["NGC5899"] = "bank=1 pix_list=-13,14,15"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
