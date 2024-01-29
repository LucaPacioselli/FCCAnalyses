# Introduction 

The purpose of this tutorial is to recreate the plot of the reconstructed invariant mass for same flavour background events (except the Z -> llnunu) from Sofia's thesis through the FCCAnalyses machinery/workflow. 

## Set Up

To start running the codes in this tutorial you need to have FCCAnalyses configured correctly somewhere (if not, follow the small paragraph "Getting started" from the README.md in `examples/FCCee/bsm/LLPs/DisplacedHNL/2HNLs`, i.e., the directory above this one)

## Pre-selection (`analysis_stage1_bkg.py`)

Analysis through FCC analyzers starts from events in EDM4hep format. In this tutorial, the reference database is the Winter 2023 campaign (http://fcc-physics-events.web.cern.ch/fcc-physics-events/FCCee/winter2023/Delphesevents_IDEA.php). It was used a 0.01 fraction of the background events we are interested in from the winter 23 campaign (order 10^8) to speed up testing. 

`outputDir`, on line 29, indicates where you want to save the output of this file. Having to deal with a large number of events you may want to put the output in Eos or a similar space.

**To run this step, do:**
```
fccanalysis run analysis_stage1_bkg.py
```

The root file output of this step (trees) will live in the specified `outputDir` directory. Open your background output with root and check that you get a tree with filled branches.

## Final selection (`analysis_final_bkg.py`)


