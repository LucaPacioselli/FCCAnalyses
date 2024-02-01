import ROOT

# global parameters
intLumi        = 150.0e+06 #in pb-1

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
scaleSig       = 0.
scaleBack      = 0.
ana_tex        = 'e^{+}e^{-} #rightarrow Z rightarrow ee#nu/mumu#nu'
delphesVersion = '3.4.2'
energy         = 91
collider       = 'FCC-ee'
inputDir       = '/eos/user/l/lpaciose/bkg2/output_finalSel/'
#formats        = ['png','pdf']
formats        = ['pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
outdir         = 'plots_durham/'
splitLeg       = True

variables = [

    #gen variables
    "n_FSGenElectron",
    "n_FSGenNeutrino",
    "n_FSGenPhoton",

    "FSGenElectron_e",
    "FSGenElectron_p",
    "FSGenElectron_pt",
    "FSGenElectron_pz",
    "FSGenElectron_eta",
    "FSGenElectron_theta",
    "FSGenElectron_phi",

    "FSGenNeutrino_e",
    "FSGenNeutrino_p",
    "FSGenNeutrino_pt",
    "FSGenNeutrino_pz",
    "FSGenNeutrino_eta",
    "FSGenNeutrino_theta",
    "FSGenNeutrino_phi",

    "FSGenPhoton_e",
    "FSGenPhoton_p",
    "FSGenPhoton_pt",
    "FSGenPhoton_pz",
    "FSGenPhoton_eta",
    "FSGenPhoton_theta",
    "FSGenPhoton_phi",

    "FSGenElectron_vertex_x",
    "FSGenElectron_vertex_y",
    "FSGenElectron_vertex_z",
    "FSGenElectron_vertex_x_prompt",
    "FSGenElectron_vertex_y_prompt",
    "FSGenElectron_vertex_z_prompt",

    "FSGen_Lxy",
    "FSGen_Lxyz",
    "FSGen_Lxyz_prompt",

    "FSGen_ee_invMass",
    "FSGen_eenu_invMass",

    #reco variables
    "n_RecoTracks",
    #"n_RecoJets",
    "n_RecoPhotons",
    "n_RecoElectrons",
    "n_RecoMuons",

    "RecoJet_e",
    "RecoJet_p",
    "RecoJet_pt",
    "RecoJet_pz",
    "RecoJet_eta",
    "RecoJet_theta",
    "RecoJet_phi",
    #"RecoJet_charge",

    #"RecoJetTrack_absD0",
    #"RecoJetTrack_absD0_prompt",
    #"RecoJetTrack_absZ0",
    #"RecoJetTrack_absZ0_prompt",
    #"RecoJetTrack_absD0sig",
    #"RecoJetTrack_absD0sig_prompt",
    #"RecoJetTrack_absZ0sig",
    #"RecoJetTrack_absZ0sig_prompt",
    #"RecoJetTrack_D0cov",
    #"RecoJetTrack_Z0cov",

    "RecoElectron_e",
    "RecoElectron_p",
    "RecoElectron_pt",
    "RecoElectron_pz",
    "RecoElectron_eta",
    "RecoElectron_theta",
    "RecoElectron_phi",
    "RecoElectron_charge",

    "RecoElectronTrack_absD0",
    "RecoElectronTrack_absD0_prompt",
    "RecoElectronTrack_absZ0",
    "RecoElectronTrack_absZ0_prompt",
    "RecoElectronTrack_absD0sig",
    "RecoElectronTrack_absD0sig_prompt",
    "RecoElectronTrack_absZ0sig",
    "RecoElectronTrack_absZ0sig_prompt",
    "RecoElectronTrack_D0cov",
    "RecoElectronTrack_Z0cov",

    "Reco_ee_invMass",
    "Reco_mumu_invMass",
    "Reco_ll_invMass",

    "RecoPhoton_e",
    "RecoPhoton_p",
    "RecoPhoton_pt",
    "RecoPhoton_pz",
    "RecoPhoton_eta",
    "RecoPhoton_theta",
    "RecoPhoton_phi",
    "RecoPhoton_charge",

    "RecoMuon_e",
    "RecoMuon_p",
    "RecoMuon_pt",
    "RecoMuon_pz",
    "RecoMuon_eta",
    "RecoMuon_theta",
    "RecoMuon_phi",
    "RecoMuon_charge",

    "RecoMuonTrack_absD0",
    "RecoMuonTrack_absD0_prompt",
    "RecoMuonTrack_absZ0",
    "RecoMuonTrack_absZ0_prompt",
    "RecoMuonTrack_absD0sig",
    "RecoMuonTrack_absD0sig_prompt",
    "RecoMuonTrack_absZ0sig",
    "RecoMuonTrack_absZ0sig_prompt",
    "RecoMuonTrack_D0cov",
    "RecoMuonTrack_Z0cov",

    "RecoMissingEnergy_e",
    "RecoMissingEnergy_p",
    "RecoMissingEnergy_pt",
    "RecoMissingEnergy_px",
    "RecoMissingEnergy_py",
    "RecoMissingEnergy_pz",
    "RecoMissingEnergy_eta",
    "RecoMissingEnergy_theta",
    "RecoMissingEnergy_phi",
    
             ]

    
###Dictionary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
selections['HNL_bkg']  = [
    "selNone",
    # "sel1FSGenEle",
    # "sel1FSGenEle_eeInvMassGt80",
    # "sel1FSGenNu",
    "sel2RecoEle",
    "sel2RecoEle_vetoes",
    # "sel2RecoEle_absD0Gt0p1",
    "sel2RecoEle_vetoes_InvMass_15_70",
    # "sel2RecoEle_vetoes_absD0Gt0p5",
    #"sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5",
]

extralabel = {}
extralabel['selNone'] = "Before selection"
# extralabel['sel1FSGenEle'] = "At least 1 final state gen electron"
# extralabel['sel1FSGenEle_eeInvMassGt80'] = "At least 1 final state gen electron, gen ee inv mass > 80 GeV"
# extralabel['sel1FSGenNu'] = "At least 1 final state gen neutrino"
extralabel['sel2RecoEle'] = "2 electrons or 2 muons"
extralabel['sel2RecoEle_vetoes'] = "2 electrons or 2 muons; No jets or photons"
# extralabel['sel2RecoEle_absD0Gt0p1'] = "2 electrons with |d_0|>0.1 mm"
extralabel["sel2RecoEle_vetoes_InvMass_15_70"] = "2 electrons or 2 muons; No jets or photons; 15 GeV < Invariant Mass of the FSLeptons < 70 GeV"
# extralabel['sel2RecoEle_vetoes_absD0Gt0p5'] = "2 electrons with |d_0|>0.1 mm; No muons, jets, or photons"
#extralabel['sel2RecoEle_vetoes_MissingEnergyGt10_absD0Gt0p5'] = "2 electrons with |d_0|>0.5 mm; No muons, jets, or photons; Missing momentum > 10 GeV"

colors = {}
# colors['HNL_eenu_30GeV_1p41e-6Ve'] = ROOT.kOrange+1
# colors['HNL_eenu_50GeV_1p41e-6Ve'] = ROOT.kRed
# colors['HNL_eenu_70GeV_1p41e-6Ve'] = ROOT.kBlue
# colors['HNL_eenu_90GeV_1p41e-6Ve'] = ROOT.kGreen+1

colors['Zbb'] = ROOT.kAzure-4
colors['Zcc'] = ROOT.kCyan-9
colors['Zud'] = ROOT.kViolet-4
colors['Zss'] = ROOT.kBlue
colors['Zmumu'] = ROOT.kRed
colors['Ztautau'] = ROOT.kRed-3
colors['Zee'] = ROOT.kGray+2

plots = {}
plots['HNL_bkg'] = {'signal':{
                    # 'HNL_eenu_30GeV_1p41e-6Ve':['HNL_eenu_30GeV_1p41e-6Ve'],
                    # 'HNL_eenu_50GeV_1p41e-6Ve':['HNL_eenu_50GeV_1p41e-6Ve'],
                    # 'HNL_eenu_70GeV_1p41e-6Ve':['HNL_eenu_70GeV_1p41e-6Ve'],
                    # 'HNL_eenu_90GeV_1p41e-6Ve':['HNL_eenu_90GeV_1p41e-6Ve'],
},
                'backgrounds':{
                    'Zbb':['p8_ee_Zbb_ecm91'],
                    'Zcc': ['p8_ee_Zcc_ecm91'],
                    'Zud': ['p8_ee_Zud_ecm91'],
                    'Zss':['p8_ee_Zss_ecm91'],
                    'Ztautau': ['p8_ee_Ztautau_ecm91'],
                    'Zee':['p8_ee_Zee_ecm91'],
                    'Zmumu':['p8_ee_Zmumu_ecm91'],
                }
                }


legend = {}
# legend['HNL_eenu_30GeV_1p41e-6Ve'] = 'm_{N} = 30 GeV, V_{e} = 1.41e-6'
# legend['HNL_eenu_50GeV_1p41e-6Ve'] = 'm_{N} = 50 GeV, V_{e} = 1.41e-6'
# legend['HNL_eenu_70GeV_1p41e-6Ve'] = 'm_{N} = 70 GeV, V_{e} = 1.41e-6'
# legend['HNL_eenu_90GeV_1p41e-6Ve'] = 'm_{N} = 90 GeV, V_{e} = 1.41e-6'

legend['Zbb'] = 'e^{+}e^{-} #rightarrow Z #rightarrow bb'
legend['Zcc'] = 'e^{+}e^{-} #rightarrow Z #rightarrow cc'
legend['Zmumu'] = 'e^{+}e^{-} #rightarrow Z #rightarrow mumu'
legend['Zud'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ud'
legend['Zss'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ss'
legend['Ztautau'] = 'e^{+}e^{-} #rightarrow Z #rightarrow #tau#tau'
legend['Zee'] = 'e^{+}e^{-} #rightarrow Z #rightarrow ee'