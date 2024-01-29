# Introduction 

The purpose of this tutorial is to recreate the plot of the reconstructed invariant mass for same flavour background events (except the Z -> llnunu) from Sofia's thesis through the FCCAnalyses machinery/workflow. 

## Set Up

To start running the codes in this tutorial you need to have FCCAnalyses configured correctly somewhere (if not, follow the small paragraph "Getting started" from the README.md in `examples/FCCee/bsm/LLPs/DisplacedHNL/2HNLs`, i.e., the directory above this one).

The in-depth and general tutorial on using FCCAnalyses for LLP HNL signals can be found in the README.md of `examples/FCCee/bsm/LLPs/DisplacedHNL`.

## Pre-selection (`analysis_stage1_bkg.py`)

Analysis through FCC analyzers starts from events in EDM4hep format. In this tutorial, the reference database is the Winter 2023 campaign (http://fcc-physics-events.web.cern.ch/fcc-physics-events/FCCee/winter2023/Delphesevents_IDEA.php). It was used a 0.01 fraction of the background events we are interested in from the winter 23 campaign (order 10^8) to speed up testing. 

The code for this step is in `analysis_stage1_bkg.py`. `outputDir`, on line 29, indicates where you want to save the output of this file. Having to deal with a large number of events you may want to put the output in Eos or a similar space.

**To run this step, do:**
```
fccanalysis run analysis_stage1_bkg.py
```

The root file output of this step (trees) will live in the specified `outputDir` directory. Open your background output with root and check that you get a tree with filled branches.

## Final selection (`analysis_final_bkg.py`)

This second step will run over the "stage 1" output and apply selections (or cut sets) to the variables of interest. For each selection, a root file will be created containing histograms. We have set up 4 cut sets:

 - **selNone** applies no selection at all
 - **sel2RecoEle** requires exactly two reconstructed electrons (or muons)
 - **sel2RecoEle_vetoes** requires exactly two reconstructed electrons (or muons) and vetoes events with any reconstructed jets or photons
 - **sel2RecoEle_vetoes_InvMass_15_70** requires exactly two reconstructed electrons (or muons); vetoes events with any reconstructed jets or photons; and requires the reconstructed invariant mass to be > 15 GeV and < 70 GeV


The code for this step is in `analysis_final_bkg.py`. 
  
To run over the large background samples from "stage1", you should do them one at a time (comment out the others in `processList` in `analysis_final_bkg.py`). The Zee and Ztautau samples will take about 10 min each, but the other backgrounds are quite big and perhaps take too much time to run locally.

**(Luca's note: I ran over the large background samples all at once and it really took me a long time).**
  
**To run this step, do:**
```
fccanalysis final analysis_final_bkg.py
```

The root file output of this step (histograms) will live in the `output_finalSel/` directory. Open your output with root and check that you get histograms.

## Make plots (`analysis_plot_inv_mass_same_bkg.py`)

This final step makes jpg and/or pdf plots of the histograms you made in the previous step.

**To run this step, do:**
```
fccanalysis plots analysis_plot_inv_mass_same_bkg.py
```

The output of this step (plots) will live in the `plots/` directory. Each subdirectory corresponds to the different selections you applied, and each plot will be saved (by default) as a pdf with both a linear and a log y-axis. You can use the `evince` command to look at a pdf on lxplus.

