#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-20"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['foo'] = [ ]
on["IC3392"] =  [ 113121, 113123, 113125,]

on["NGC4189"] = [ 113113, 113115, 113117,]

on["NGC5347"] = [ 112756, 112758, 112760, 112762, 112764, 112770, 112772,
                  112774, 112776, 112778, 112871, 112958, 112960,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["IC3392"] = ""
pars1["NGC4189"] = ""
pars1["NGC5347"] = ""


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["IC3392"] = ""
pars2["NGC4189"] = ""
pars2["NGC5347"] = ""


#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["IC3392"] = ""
pars3["NGC4189"] = ""
pars3["NGC5347"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
