#Mandatory: List of processes
processList = {
        'p8_ee_Zee_ecm91':{'fraction':0.01,'chunks':100},
        'p8_ee_Zmumu_ecm91':{'fraction':0.01,'chunks':100},
        'p8_ee_Ztautau_ecm91':{'fraction':0.01,'chunks':100},
        'p8_ee_Zbb_ecm91':{'fraction':0.01,'chunks':100},
        'p8_ee_Zss_ecm91':{'fraction':0.01,'chunks':100},
        'p8_ee_Zud_ecm91':{'fraction':0.01,'chunks':100},
        'p8_ee_Zcc_ecm91':{'fraction':0.01,'chunks':100},
        #background ee_Zllnunu_ecm91

        #test
        #'p8_ee_Zuds_ecm91':{'fraction':0.000001},
        #'p8_ee_Zuds_ecm91':{'chunks':10,'fraction':0.000001},
}

#Mandatory: Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics
#prodTag     = "FCCee/winter2023/IDEA/"

# Define the input dir (optional)
#inputDir    = "outputs/FCCee/higgs/mH-recoil/mumu/stage1"
inputDir    = "/eos/experiment/fcc/ee/generation/DelphesEvents/winter2023/IDEA/"

# Link to the dictonary that contains all the cross section informations etc... (mandatory)
procDict = "FCCee_procDict_winter2023_IDEA.json"

#Optional: output directory, default is local dir
#outputDir = "/eos/experiment/fcc/ee/analyses/case-studies/bsm/LLPs/HNLs/"
outputDir = "/eos/user/l/lpaciose/bkg"
#outputDir = "output_stage1/"

#outputDirEos = "/eos/user/l/lpaciose/bkg"
#outputDirEos = "/eos/user/j/jalimena/FCCeeLLP/"
#eosType = "eosuser"

#Optional: ncpus, default is 4. 
nCPUS       = 4

#Optional running on HTCondor, default is False
runBatch    = False
#runBatch    = True

#Optional batch queue name when running on HTCondor, default is workday
#batchQueue = "longlunch"

#Optional computing account when running on HTCondor, default is group_u_FCC.local_gen
#compGroup = "group_u_FCC.local_gen"

#Mandatory: RDFanalysis class where the use defines the operations on the TTree
class RDFanalysis():
        def analysers(df):

                #Access the various objects and their properties with the following syntax: .Define("<your_variable>", "<accessor_fct (name_object)>")
		#This will create a column in the RDataFrame named <your_variable> and filled with the return value of the <accessor_fct> for the given collection/object 
		#Accessor functions are the functions found in the C++ analyzers code that return a certain variable, e.g. <namespace>::get_n(object) returns the number 
		#of these objects in the event and <namespace>::get_pt(object) returns the pt of the object. Here you can pick between two namespaces to access either
		#reconstructed (namespace = ReconstructedParticle) or MC-level objects (namespace = MCParticle). 
		#For the name of the object, in principle the names of the EDM4HEP collections are used - photons, muons and electrons are an exception, see below

		#OVERVIEW: Accessing different objects and counting them
               

            # Following code is written specifically for the HNL study
            ####################################################################################################
            df = df.Alias("Particle1", "Particle#1.index")
            df = df.Alias("MCRecoAssociations0", "MCRecoAssociations#0.index")
            df = df.Alias("MCRecoAssociations1", "MCRecoAssociations#1.index")
 
            #all final state gen electrons and positrons
            df = df.Define("GenElectron_PID", "FCCAnalyses::MCParticle::sel_pdgID(11, true)(Particle)")
            df = df.Define("FSGenElectron", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenElectron_PID)") #gen status==1 means final state particle (FS)
            df = df.Define("n_FSGenElectron", "FCCAnalyses::MCParticle::get_n(FSGenElectron)")
            #put in dummy values below if there aren't any FSGenElectrons, to avoid seg fault
            df = df.Define("FSGenElectron_e", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_e(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_p", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_p(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_pt", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_pt(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_px", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_px(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_py", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_py(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_pz", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_pz(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_eta", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_eta(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_theta", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_theta(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_phi", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_phi(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_charge", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_charge(FSGenElectron); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")

            df = df.Define("FSGenElectron_vertex_x", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_vertex_x( FSGenElectron ); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_vertex_y", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_vertex_y( FSGenElectron ); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")
            df = df.Define("FSGenElectron_vertex_z", "if (n_FSGenElectron>0) return FCCAnalyses::MCParticle::get_vertex_z( FSGenElectron ); else return FCCAnalyses::MCParticle::get_genStatus(GenElectron_PID);")

            #all final state gen muons and anti-muons
            df = df.Define("GenMuon_PID", "FCCAnalyses::MCParticle::sel_pdgID(13, true)(Particle)")
            df = df.Define("FSGenMuon", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenMuon_PID)") #gen status==1 means final state particle (FS)
            df = df.Define("n_FSGenMuon", "FCCAnalyses::MCParticle::get_n(FSGenMuon)")
            #put in dummy values below if there aren't any FSGenMuon, to avoid seg fault
            df = df.Define("FSGenMuon_e", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_e(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_p", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_p(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_pt", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_pt(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_px", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_px(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_py", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_py(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_pz", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_pz(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_eta", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_eta(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_theta", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_theta(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_phi", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_phi(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_charge", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_charge(FSGenMuon); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")

            df = df.Define("FSGenMuon_vertex_x", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_vertex_x( FSGenMuon ); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_vertex_y", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_vertex_y( FSGenMuon ); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")
            df = df.Define("FSGenMuon_vertex_z", "if (n_FSGenMuon>0) return FCCAnalyses::MCParticle::get_vertex_z( FSGenMuon ); else return FCCAnalyses::MCParticle::get_genStatus(GenMuon_PID);")


            # Finding the Lxy of the HNL
            # Definition: Lxy = math.sqrt( (branchGenPtcl.At(daut1).X)**2 + (branchGenPtcl.At(daut1).Y)**2 )
            df = df.Define("FSGen_Lxy", "return sqrt(FSGenElectron_vertex_x*FSGenElectron_vertex_x + FSGenElectron_vertex_y*FSGenElectron_vertex_y)")
            # Finding the Lxyz of the HNL
            df = df.Define("FSGen_Lxyz", "return sqrt(FSGenElectron_vertex_x*FSGenElectron_vertex_x + FSGenElectron_vertex_y*FSGenElectron_vertex_y + FSGenElectron_vertex_z*FSGenElectron_vertex_z)")

            #all final state gen neutrinos and anti-neutrinos
            df = df.Define("GenNeutrino_PID", "FCCAnalyses::MCParticle::sel_pdgID(12, true)(Particle)")
            df = df.Define("FSGenNeutrino", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenNeutrino_PID)") #gen status==1 means final state particle (FS)
            df = df.Define("n_FSGenNeutrino", "FCCAnalyses::MCParticle::get_n(FSGenNeutrino)")
            df = df.Define("FSGenNeutrino_e", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_e(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_p", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_p(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_pt", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_pt(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_px", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_px(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_py", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_py(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_pz", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_pz(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_eta", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_eta(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_theta", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_theta(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_phi", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_phi(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")
            df = df.Define("FSGenNeutrino_charge", "if (n_FSGenNeutrino>0) return FCCAnalyses::MCParticle::get_charge(FSGenNeutrino); else return FCCAnalyses::MCParticle::get_genStatus(GenNeutrino_PID);")

            #all final state gen photons
            df = df.Define("GenPhoton_PID", "FCCAnalyses::MCParticle::sel_pdgID(22, false)(Particle)")
            df = df.Define("FSGenPhoton", "FCCAnalyses::MCParticle::sel_genStatus(1)(GenPhoton_PID)") #gen status==1 means final state particle (FS)
            df = df.Define("n_FSGenPhoton", "FCCAnalyses::MCParticle::get_n(FSGenPhoton)")
            df = df.Define("FSGenPhoton_e", "FCCAnalyses::MCParticle::get_e(FSGenPhoton)")
            df = df.Define("FSGenPhoton_p", "FCCAnalyses::MCParticle::get_p(FSGenPhoton)")
            df = df.Define("FSGenPhoton_pt", "FCCAnalyses::MCParticle::get_pt(FSGenPhoton)")
            df = df.Define("FSGenPhoton_px", "FCCAnalyses::MCParticle::get_px(FSGenPhoton)")
            df = df.Define("FSGenPhoton_py", "FCCAnalyses::MCParticle::get_py(FSGenPhoton)")
            df = df.Define("FSGenPhoton_pz", "FCCAnalyses::MCParticle::get_pz(FSGenPhoton)")
            df = df.Define("FSGenPhoton_eta", "FCCAnalyses::MCParticle::get_eta(FSGenPhoton)")
            df = df.Define("FSGenPhoton_theta", "FCCAnalyses::MCParticle::get_theta(FSGenPhoton)")
            df = df.Define("FSGenPhoton_phi", "FCCAnalyses::MCParticle::get_phi(FSGenPhoton)")
            df = df.Define("FSGenPhoton_charge", "FCCAnalyses::MCParticle::get_charge(FSGenPhoton)")


            # ee invariant mass
            df = df.Define("FSGen_ee_energy", "if (n_FSGenElectron>1) return (FSGenElectron_e.at(0) + FSGenElectron_e.at(1)); else return float(-1.);")
            df = df.Define("FSGen_ee_px", "if (n_FSGenElectron>1) return (FSGenElectron_px.at(0) + FSGenElectron_px.at(1)); else return float(-1.);")
            df = df.Define("FSGen_ee_py", "if (n_FSGenElectron>1) return (FSGenElectron_py.at(0) + FSGenElectron_py.at(1)); else return float(-1.);")
            df = df.Define("FSGen_ee_pz", "if (n_FSGenElectron>1) return (FSGenElectron_pz.at(0) + FSGenElectron_pz.at(1)); else return float(-1.);")
            df = df.Define("FSGen_ee_invMass", "if (n_FSGenElectron>1) return sqrt(FSGen_ee_energy*FSGen_ee_energy - FSGen_ee_px*FSGen_ee_px - FSGen_ee_py*FSGen_ee_py - FSGen_ee_pz*FSGen_ee_pz ); else return float(-1.);")

            # mumu invariant mass
            df = df.Define("FSGen_mumu_energy", "if (n_FSGenMuon>1) return (FSGenMuon_e.at(0) + FSGenMuon_e.at(1)); else return float(-1.);")
            df = df.Define("FSGen_mumu_px", "if (n_FSGenMuon>1) return (FSGenMuon_px.at(0) + FSGenMuon_px.at(1)); else return float(-1.);")
            df = df.Define("FSGen_mumu_py", "if (n_FSGenMuon>1) return (FSGenMuon_py.at(0) + FSGenMuon_py.at(1)); else return float(-1.);")
            df = df.Define("FSGen_mumu_pz", "if (n_FSGenMuon>1) return (FSGenMuon_pz.at(0) + FSGenMuon_pz.at(1)); else return float(-1.);")
            df = df.Define("FSGen_mumu_invMass", "if (n_FSGenMuon>1) return sqrt(FSGen_mumu_energy*FSGen_mumu_energy - FSGen_mumu_px*FSGen_mumu_px - FSGen_mumu_py*FSGen_mumu_py - FSGen_mumu_pz*FSGen_mumu_pz ); else return float(-1.);")

            # eenu invariant mass
            df = df.Define("FSGen_eenu_energy", "if (n_FSGenElectron>1 && n_FSGenNeutrino>0) return (FSGenElectron_e.at(0) + FSGenElectron_e.at(1) + FSGenNeutrino_e.at(0)); else return float(-1.);")
            df = df.Define("FSGen_eenu_px", "if (n_FSGenElectron>1 && n_FSGenNeutrino>0) return (FSGenElectron_px.at(0) + FSGenElectron_px.at(1) + FSGenNeutrino_px.at(0)); else return float(-1.);")
            df = df.Define("FSGen_eenu_py", "if (n_FSGenElectron>1 && n_FSGenNeutrino>0) return (FSGenElectron_py.at(0) + FSGenElectron_py.at(1) + FSGenNeutrino_py.at(0)); else return float(-1.);")
            df = df.Define("FSGen_eenu_pz", "if (n_FSGenElectron>1 && n_FSGenNeutrino>0) return (FSGenElectron_pz.at(0) + FSGenElectron_pz.at(1) + FSGenNeutrino_pz.at(0)); else return float(-1.);")
            df = df.Define("FSGen_eenu_invMass", "if (n_FSGenElectron>1 && n_FSGenNeutrino>0) return sqrt(FSGen_eenu_energy*FSGen_eenu_energy - FSGen_eenu_px*FSGen_eenu_px - FSGen_eenu_py*FSGen_eenu_py - FSGen_eenu_pz*FSGen_eenu_pz ); else return float(-1.);")
                


            # MC event primary vertex
            df = df.Define("MC_PrimaryVertex",  "FCCAnalyses::MCParticle::get_EventPrimaryVertex(21)( Particle )" )

            # Reconstructed particles
            df = df.Define("n_RecoTracks","ReconstructedParticle2Track::getTK_n(EFlowTrack_1)")
                
		    #JETS
			
            df = df.Define("n_RecoJets","ReconstructedParticle::get_n(Jet)") #count how many jets are in the event in total

		    #PHOTONS
			
            df = df.Alias("Photon0", "Photon#0.index")
			
            df = df.Define("RecoPhotons",  "ReconstructedParticle::get(Photon0, ReconstructedParticles)")
			
            df = df.Define("n_RecoPhotons",  "ReconstructedParticle::get_n(RecoPhotons)") #count how many photons are in the event in total

		    #ELECTRONS AND MUONS
		    
            df = df.Alias("Electron0", "Electron#0.index")
		    
            df = df.Define("RecoElectrons",  "ReconstructedParticle::get(Electron0, ReconstructedParticles)")
		    
            df = df.Define("n_RecoElectrons",  "ReconstructedParticle::get_n(RecoElectrons)") #count how many electrons are in the event in total

		    
            df = df.Alias("Muon0", "Muon#0.index")
		    
            df = df.Define("RecoMuons",  "ReconstructedParticle::get(Muon0, ReconstructedParticles)")
    		
            df = df.Define("n_RecoMuons",  "ReconstructedParticle::get_n(RecoMuons)") #count how many muons are in the event in total

		    #SIMPLE VARIABLES: Access the basic kinematic variables of the (selected) jets, works analogously for electrons, muons
		    
            df = df.Define("RecoJet_e",      "ReconstructedParticle::get_e(Jet)")
            df = df.Define("RecoJet_p",      "ReconstructedParticle::get_p(Jet)") #momentum p
            df = df.Define("RecoJet_pt",      "ReconstructedParticle::get_pt(Jet)") #transverse momentum pt
            df = df.Define("RecoJet_px",      "ReconstructedParticle::get_px(Jet)")
            df = df.Define("RecoJet_py",      "ReconstructedParticle::get_py(Jet)")
            df = df.Define("RecoJet_pz",      "ReconstructedParticle::get_pz(Jet)")
		    
            df = df.Define("RecoJet_eta",     "ReconstructedParticle::get_eta(Jet)") #pseudorapidity eta
            df = df.Define("RecoJet_theta",   "ReconstructedParticle::get_theta(Jet)")
		    
            df = df.Define("RecoJet_phi",     "ReconstructedParticle::get_phi(Jet)") #polar angle in the transverse plane phi
            df = df.Define("RecoJet_charge",  "ReconstructedParticle::get_charge(Jet)")
            df = df.Define("RecoJetTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(Jet,EFlowTrack_1))")
            df = df.Define("RecoJetTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(Jet,EFlowTrack_1))")
            
            df = df.Define("RecoJetTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(Jet,EFlowTrack_1))") #significance
            df = df.Define("RecoJetTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(Jet,EFlowTrack_1))")
            
            df = df.Define("RecoJetTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(Jet,EFlowTrack_1)") #variance (not sigma)
            df = df.Define("RecoJetTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(Jet,EFlowTrack_1)")

            df = df.Define("RecoElectron_e",      "ReconstructedParticle::get_e(RecoElectrons)")
            df = df.Define("RecoElectron_p",      "ReconstructedParticle::get_p(RecoElectrons)")
            df = df.Define("RecoElectron_pt",      "ReconstructedParticle::get_pt(RecoElectrons)")
            df = df.Define("RecoElectron_px",      "ReconstructedParticle::get_px(RecoElectrons)")
            df = df.Define("RecoElectron_py",      "ReconstructedParticle::get_py(RecoElectrons)")
            df = df.Define("RecoElectron_pz",      "ReconstructedParticle::get_pz(RecoElectrons)")
		    
            df = df.Define("RecoElectron_eta",     "ReconstructedParticle::get_eta(RecoElectrons)") #pseudorapidity eta
            df = df.Define("RecoElectron_theta",   "ReconstructedParticle::get_theta(RecoElectrons)")
		    
            df = df.Define("RecoElectron_phi",     "ReconstructedParticle::get_phi(RecoElectrons)") #polar angle in the transverse plane phi
            df = df.Define("RecoElectron_charge",  "ReconstructedParticle::get_charge(RecoElectrons)")
            df = df.Define("RecoElectronTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoElectrons,EFlowTrack_1))")
            df = df.Define("RecoElectronTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoElectrons,EFlowTrack_1))")
            df = df.Define("RecoElectronTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoElectrons,EFlowTrack_1))") #significance
            df = df.Define("RecoElectronTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoElectrons,EFlowTrack_1))")
            df = df.Define("RecoElectronTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoElectrons,EFlowTrack_1)") #variance (not sigma)
            df = df.Define("RecoElectronTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoElectrons,EFlowTrack_1)")

            df = df.Define("RecoElectronTracks",   "ReconstructedParticle2Track::getRP2TRK( RecoElectrons, EFlowTrack_1)")

            # Now we reconstruct the reco decay vertex using the reco'ed tracks from electrons
            # First the full object, of type Vertexing::FCCAnalysesVertex
            df = df.Define("RecoDecayVertexObject",   "VertexFitterSimple::VertexFitter_Tk( 2, RecoElectronTracks)" )

            # from which we extract the edm4hep::VertexData object, which contains the vertex position in mm
            df = df.Define("RecoDecayVertex",  "VertexingUtils::get_VertexData( RecoDecayVertexObject )")

            df = df.Define("Reco_Lxy", "return sqrt(RecoDecayVertex.position.x*RecoDecayVertex.position.x + RecoDecayVertex.position.y*RecoDecayVertex.position.y)")
            df = df.Define("Reco_Lxyz","return sqrt(RecoDecayVertex.position.x*RecoDecayVertex.position.x + RecoDecayVertex.position.y*RecoDecayVertex.position.y + RecoDecayVertex.position.z*RecoDecayVertex.position.z)")

            df = df.Define("RecoPhoton_e",      "ReconstructedParticle::get_e(RecoPhotons)")
            df = df.Define("RecoPhoton_p",      "ReconstructedParticle::get_p(RecoPhotons)")
            df = df.Define("RecoPhoton_pt",      "ReconstructedParticle::get_pt(RecoPhotons)")
            df = df.Define("RecoPhoton_px",      "ReconstructedParticle::get_px(RecoPhotons)")
            df = df.Define("RecoPhoton_py",      "ReconstructedParticle::get_py(RecoPhotons)")
            df = df.Define("RecoPhoton_pz",      "ReconstructedParticle::get_pz(RecoPhotons)")
		    
            df = df.Define("RecoPhoton_eta",     "ReconstructedParticle::get_eta(RecoPhotons)") #pseudorapidity eta
            
            df = df.Define("RecoPhoton_theta",   "ReconstructedParticle::get_theta(RecoPhotons)")
		    
            df = df.Define("RecoPhoton_phi",     "ReconstructedParticle::get_phi(RecoPhotons)") #polar angle in the transverse plane phi
            
            df = df.Define("RecoPhoton_charge",  "ReconstructedParticle::get_charge(RecoPhotons)")

            df = df.Define("RecoMuon_e",      "ReconstructedParticle::get_e(RecoMuons)")
            df = df.Define("RecoMuon_p",      "ReconstructedParticle::get_p(RecoMuons)")
            df = df.Define("RecoMuon_pt",      "ReconstructedParticle::get_pt(RecoMuons)")
            df = df.Define("RecoMuon_px",      "ReconstructedParticle::get_px(RecoMuons)")
            df = df.Define("RecoMuon_py",      "ReconstructedParticle::get_py(RecoMuons)")
            df = df.Define("RecoMuon_pz",      "ReconstructedParticle::get_pz(RecoMuons)")
		    
            df = df.Define("RecoMuon_eta",     "ReconstructedParticle::get_eta(RecoMuons)") #pseudorapidity eta
            df = df.Define("RecoMuon_theta",   "ReconstructedParticle::get_theta(RecoMuons)")
		    
            df = df.Define("RecoMuon_phi",     "ReconstructedParticle::get_phi(RecoMuons)") #polar angle in the transverse plane phi
            df = df.Define("RecoMuon_charge",  "ReconstructedParticle::get_charge(RecoMuons)")
            df = df.Define("RecoMuonTrack_absD0", "return abs(ReconstructedParticle2Track::getRP2TRK_D0(RecoMuons,EFlowTrack_1))")
            df = df.Define("RecoMuonTrack_absZ0", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0(RecoMuons,EFlowTrack_1))")
            df = df.Define("RecoMuonTrack_absD0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_D0_sig(RecoMuons,EFlowTrack_1))") #significance
            df = df.Define("RecoMuonTrack_absZ0sig", "return abs(ReconstructedParticle2Track::getRP2TRK_Z0_sig(RecoMuons,EFlowTrack_1))")
            df = df.Define("RecoMuonTrack_D0cov", "ReconstructedParticle2Track::getRP2TRK_D0_cov(RecoMuons,EFlowTrack_1)") #variance (not sigma)
            df = df.Define("RecoMuonTrack_Z0cov", "ReconstructedParticle2Track::getRP2TRK_Z0_cov(RecoMuons,EFlowTrack_1)")
			
            #EVENTWIDE VARIABLES: Access quantities that exist only once per event, such as the missing energy (despite the name, the MissingET collection contains the total missing energy)
		    
            df = df.Define("RecoMissingEnergy_e", "ReconstructedParticle::get_e(MissingET)")
		    
            df = df.Define("RecoMissingEnergy_p", "ReconstructedParticle::get_p(MissingET)")
		    
            df = df.Define("RecoMissingEnergy_pt", "ReconstructedParticle::get_pt(MissingET)")
		    
            df = df.Define("RecoMissingEnergy_px", "ReconstructedParticle::get_px(MissingET)") #x-component of RecoMissingEnergy
		    
            df = df.Define("RecoMissingEnergy_py", "ReconstructedParticle::get_py(MissingET)") #y-component of RecoMissingEnergy
		    
            df = df.Define("RecoMissingEnergy_pz", "ReconstructedParticle::get_pz(MissingET)") #z-component of RecoMissingEnergy
		    
            df = df.Define("RecoMissingEnergy_eta", "ReconstructedParticle::get_eta(MissingET)")
		    
            df = df.Define("RecoMissingEnergy_theta", "ReconstructedParticle::get_theta(MissingET)")
		    
            df = df.Define("RecoMissingEnergy_phi", "ReconstructedParticle::get_phi(MissingET)") #angle of RecoMissingEnergy

            # ee invariant mass
            
            df = df.Define("Reco_ee_energy", "if (n_RecoElectrons>1) return (RecoElectron_e.at(0) + RecoElectron_e.at(1)); else return float(-1.);")
            df = df.Define("Reco_ee_px", "if (n_RecoElectrons>1) return (RecoElectron_px.at(0) + RecoElectron_px.at(1)); else return float(-1.);")
            df = df.Define("Reco_ee_py", "if (n_RecoElectrons>1) return (RecoElectron_py.at(0) + RecoElectron_py.at(1)); else return float(-1.);")
            df = df.Define("Reco_ee_pz", "if (n_RecoElectrons>1) return (RecoElectron_pz.at(0) + RecoElectron_pz.at(1)); else return float(-1.);")
            df = df.Define("Reco_ee_invMass", "if (n_RecoElectrons>1) return sqrt(Reco_ee_energy*Reco_ee_energy - Reco_ee_px*Reco_ee_px - Reco_ee_py*Reco_ee_py - Reco_ee_pz*Reco_ee_pz ); else return float(-1.);")

            #mumu invariant mass 
            
            df = df.Define("Reco_mumu_energy", "if (n_RecoMuons>1) return (RecoMuon_e.at(0) + RecoMuon_e.at(1)); else return float(-1.);")
            df = df.Define("Reco_mumu_px", "if (n_RecoMuons>1) return (RecoMuon_px.at(0) + RecoMuon_px.at(1)); else return float(-1.);")
            df = df.Define("Reco_mumu_py", "if (n_RecoMuons>1) return (RecoMuon_py.at(0) + RecoMuon_py.at(1)); else return float(-1.);")
            df = df.Define("Reco_mumu_pz", "if (n_RecoMuons>1) return (RecoMuon_pz.at(0) + RecoMuon_pz.at(1)); else return float(-1.);")
            df = df.Define("Reco_mumu_invMass", "if (n_RecoMuons>1) return sqrt(Reco_mumu_energy*Reco_mumu_energy - Reco_mumu_px*Reco_mumu_px - Reco_mumu_py*Reco_mumu_py - Reco_mumu_pz*Reco_mumu_pz ); else return float(-1.);")


                
            return df

        def output():
                branchList = [
                        ######## Monte-Carlo particles #######
                        "n_FSGenElectron",
                        "FSGenElectron_e",
                        "FSGenElectron_p",
                        "FSGenElectron_pt",
                        "FSGenElectron_px",
                        "FSGenElectron_py",
                        "FSGenElectron_pz",
                        "FSGenElectron_eta",
                        "FSGenElectron_theta",
                        "FSGenElectron_phi",
                        "FSGenElectron_charge",
                        "FSGenElectron_vertex_x",
                        "FSGenElectron_vertex_y",
                        "FSGenElectron_vertex_z",
                        "FSGen_Lxy",
                        "FSGen_Lxyz",
                        "n_FSGenNeutrino",
                        "FSGenNeutrino_e",
                        "FSGenNeutrino_p",
                        "FSGenNeutrino_pt",
                        "FSGenNeutrino_px",
                        "FSGenNeutrino_py",
                        "FSGenNeutrino_pz",
                        "FSGenNeutrino_eta",
                        "FSGenNeutrino_theta",
                        "FSGenNeutrino_phi",
                        "FSGenNeutrino_charge",
                        "n_FSGenPhoton",
                        "FSGenPhoton_e",
                        "FSGenPhoton_p",
                        "FSGenPhoton_pt",
                        "FSGenPhoton_px",
                        "FSGenPhoton_py",
                        "FSGenPhoton_pz",
                        "FSGenPhoton_eta",
                        "FSGenPhoton_theta",
                        "FSGenPhoton_phi",
                        "FSGenPhoton_charge",

                        ######## Reconstructed particles #######
                        "n_RecoTracks",
                        "n_RecoJets",
                        "n_RecoPhotons",
                        "n_RecoElectrons",
                        "n_RecoMuons",
                        "RecoJet_e",
                        "RecoJet_p",
                        "RecoJet_pt",
                        "RecoJet_px",
                        "RecoJet_py",
                        "RecoJet_pz",
                        "RecoJet_eta",
                        "RecoJet_theta",
                        "RecoJet_phi",
                        "RecoJet_charge",
                        "RecoJetTrack_absD0",
                        "RecoJetTrack_absZ0",
                        "RecoJetTrack_absD0sig",
                        "RecoJetTrack_absZ0sig",
                        "RecoJetTrack_D0cov",
                        "RecoJetTrack_Z0cov",
                        "RecoPhoton_e",
                        "RecoPhoton_p",
                        "RecoPhoton_pt",
                        "RecoPhoton_px",
                        "RecoPhoton_py",
                        "RecoPhoton_pz",
                        "RecoPhoton_eta",
                        "RecoPhoton_theta",
                        "RecoPhoton_phi",
                        "RecoPhoton_charge",
                        "RecoElectron_e",
                        "RecoElectron_p",
                        "RecoElectron_pt",
                        "RecoElectron_px",
                        "RecoElectron_py",
                        "RecoElectron_pz",
                        "RecoElectron_eta",
                        "RecoElectron_theta",
                        "RecoElectron_phi",
                        "RecoElectron_charge",
                        "RecoElectronTrack_absD0",
                        "RecoElectronTrack_absZ0",
                        "RecoElectronTrack_absD0sig",
                        "RecoElectronTrack_absZ0sig",
                        "RecoElectronTrack_D0cov",
                        "RecoElectronTrack_Z0cov",
                        "RecoDecayVertexObject",
                        "RecoDecayVertex",
                        "Reco_Lxy",
                        "Reco_Lxyz",
                        "RecoMuon_e",
                        "RecoMuon_p",
                        "RecoMuon_pt",
                        "RecoMuon_px",
                        "RecoMuon_py",
                        "RecoMuon_pz",
                        "RecoMuon_eta",
                        "RecoMuon_theta",
                        "RecoMuon_phi",
                        "RecoMuon_charge",
                        "RecoMuonTrack_absD0",
                        "RecoMuonTrack_absZ0",
                        "RecoMuonTrack_absD0sig",
                        "RecoMuonTrack_absZ0sig",
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

                        # enunu branches
                        "FSGen_ee_invMass",
                        "FSGen_eenu_invMass",
                        "Reco_ee_invMass",
                        "Reco_mumu_invMass",

		]

                return branchList