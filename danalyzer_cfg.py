import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltHM = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHM.HLTPaths = ['HLT_PAJet*_NoJetID_v*']
#,'HLT_PAFullTrack*_v*']
process.hltHM.andOr = cms.bool(True)
process.hltHM.throw = cms.bool(False)

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("FWCore.MessageService.MessageLogger_cfi")
process.GlobalTag.globaltag = 'GR_P_V43D::All'  

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
	
		# Pure Samples of D and D0 with ~2000 events
#	'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DReco/DGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO.root'
#	'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DReco/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO.root'
	
		 # Pure Samples of DPlus with 5000 events per file 16 files total/~200 files 
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_9_1_WUx.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_99_1_IPm.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_98_1_fV0.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_97_1_G1X.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_96_1_iJz.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_95_1_pmt.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_94_1_sb2.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_93_1_Im3.root',
   #    'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_92_1_dFP.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_91_1_Fx1.root',
 #      'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_90_1_SwQ.root',
     #  'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_8_1_YZN.root',
    #   'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_89_1_oQp.root',
   #    'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_88_1_ALJ.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_87_1_vwu.root',
 #      'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_86_1_Stg.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_v1/DPlusGun_pythia6_GEN_SIM_RECO_v1//88e9ed75f72d3c8778d7e1ca2e731a08/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_85_1_oLL.root'

		#Kalman and Addaptive Vertex Fitter for Pure Samples of DPlus with 5000 events/file and 26 files/188
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_100_1_Ykz.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_101_1_tQi.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_102_1_whb.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_9_1_hXb.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_103_1_R1y.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_99_1_0qq.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_104_1_I6k.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_98_1_PID.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_105_1_VYG.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_97_1_rCr.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_106_1_ILb.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_96_1_ve0.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_107_1_Ef5.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_95_1_kvS.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_108_1_Xlm.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_94_1_L6r.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_109_1_UD0.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_93_1_XV2.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_10_1_vT3.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_92_1_WhU.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_110_1_69m.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_91_1_qCX.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_111_1_Mu5.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_90_1_ful.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_112_1_QSq.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_8_1_87L.root',
#       '/store/user/davidlw/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1/DPlusGun_pythia6_GEN_SIM_RECO_BothVertexing_v1//b128308c6e612083e7ea4d99274185a0/DPlusGun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_113_1_COZ.root',
       

		# Pure Samples of D0 with 5000 events per file 23 files total/~200 files
#        'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_100_1_MyI.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_101_1_FDK.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_102_1_laQ.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_103_1_45Y.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_104_1_wmL.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_105_1_FRt.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_9_1_kop.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_106_1_czG.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_99_1_woa.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_107_1_Xd4.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_98_1_LVw.root'
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_108_1_858.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_97_1_WoM.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_109_1_7Tm.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_96_1_djQ.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_10_1_V7n.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_95_1_4K9.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_110_1_Unk.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_94_1_aSd.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_111_1_lJX.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_93_1_5WH.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_112_1_Nzb.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_92_1_fX8.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_v1/D0Gun_pythia6_GEN_SIM_RECO_v1//e3b81e3804a0db491e0215c536bd6aa9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_113_1_ieW.root'

		# D0 Signal with Kalman and Addaptive vertex reco 20 files with 5000/file
	
#	'/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_100_1_klS.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_101_1_qs6.root'
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_102_1_jG1.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_103_1_qpC.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_104_1_gmr.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_105_1_cuv.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_106_1_qx1.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_107_1_RA7.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_108_1_EnT.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_109_1_rs3.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_10_1_bbr.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_110_1_c8t.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_111_1_K6B.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_112_1_8Ws.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_113_1_4sV.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_114_1_Qf1.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_115_1_8rl.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_116_1_ND6.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_117_1_nS6.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_118_1_SZS.root',
#       '/store/user/davidlw/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1/D0Gun_pythia6_GEN_SIM_RECO_BothVertexing_v1//111d1818259e8a713e18193d8f6b76e9/D0Gun_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_119_1_mmo.root',

		# Pure Background with 45000 events from 45 files
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_106_2_Nu2.root',
#      'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_122_1_uDm.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_138_2_0mX.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_154_2_FdF.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_170_2_tW8.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_173_2_X1v.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_17_2_jwN.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_180_2_Snc.root',
#      'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_182_2_HHj.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_19_2_x4X.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_203_1_MRC.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_213_2_NFb.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_21_2_xu3.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_98_2_b5L.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_222_1_WLy.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_96_2_mXr.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_224_2_BKv.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_94_2_iZh.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_23_2_D46.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_92_2_8hw.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_25_2_f5z.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_90_2_1Re.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_27_2_8nq.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_88_1_tOQ.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_29_2_D1a.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_86_2_zH7.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_31_1_aSd.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_81_2_78n.root'
##       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_37_2_MBr.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_79_1_Rdh.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_3_2_aC4.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_77_2_p1s.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_41_2_yzw.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_73_2_1aw.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_45_1_p6W.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_71_1_XtE.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_47_2_dc4.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_69_2_NQc.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_49_2_54x.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_63_2_eXa.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_4_2_QRX.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_57_2_KiZ.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_51_1_mwm.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_55_2_gVw.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/HIJING_RECO_YUE-SHI_Minbias_1_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_53_2_wz7.root'
#
		# Pure Background with 37 files and 1000 events per file 
#	'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_100_1_Y3O.root',
 #      'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_101_1_DpY.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_103_1_coS.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_105_1_jvt.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_106_1_V0V.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_107_1_8fd.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_108_1_gl4.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_109_1_ww8.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_10_2_5DC.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_110_1_l0U.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_111_1_Ayg.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_112_1_HXl.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_113_1_0KK.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_114_1_1a5.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_115_2_g97.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_116_2_PzO.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_117_1_6Kd.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_118_1_0wW.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_119_2_eOW.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_11_2_q7E.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_120_1_IDV.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_121_1_9dx.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_122_1_LTG.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_123_1_rCB.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_124_1_FNB.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_125_1_UGP.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_126_1_5Wj.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_127_1_inl.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_128_1_5uE.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_129_1_TaJ.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_12_2_Re2.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_130_1_Kr0.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_131_1_0ob.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_132_1_qV1.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_133_1_tzJ.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_134_1_sDJ.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_135_1_noY.root',
  #     'root://xrootd1.cmsaf.mit.edu//store/user/vzhukova/HIJING_GEN-SIM_YUE-SHI_Minbias_2_v1/HIJING_RECO_YUE-SHI_Minbias__2_v1/b7d33bba7673cdb1ee6f4983c0800c79/hijing_reco_fix_136_1_ZeU.root',	

		# Embedded data with background plus D0 signal. 45 Files with 5000/file.
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_9_1_wGJ.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_8_1_SZB.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_7_1_zNt.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_6_1_LIx.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_5_1_BBW.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_4_1_Lxw.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_45_1_rrC.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_44_1_WNn.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_43_1_n2n.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_42_1_YmN.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_41_1_PDK.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_40_1_E03.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_3_1_Twv.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_39_1_ekC.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_38_1_y1P.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_37_1_VoT.root'
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_36_1_CRg.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_35_1_SND.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_34_1_4CP.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_33_1_Ujh.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_32_1_EgG.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_31_1_iEb.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_30_1_grj.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_2_1_GYN.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_29_1_RhD.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_28_1_C4W.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_27_1_L4I.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_26_1_AHu.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_25_1_fBt.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_24_1_g3m.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_23_1_QYv.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_22_1_uUD.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_21_1_ZnQ.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_20_1_CPA.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_1_1_u0J.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_19_1_SdK.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_18_1_qpd.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_17_1_jW8.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_16_1_E0K.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_15_1_QAi.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_14_1_dPh.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_13_1_XM3.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_12_1_Qqn.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_11_1_Z8q.root',
      # 'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/D0Gun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_10_1_v2Y.root' 

		# Embedded data with Dplus signal, 46 files with 5000/file.
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_10_1_twN.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_11_1_WQ7.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_12_1_nTp.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_13_1_aRB.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_14_1_PM8.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_15_1_Qwc.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_16_1_FcJ.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_17_1_nXk.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_18_1_B9R.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_19_1_W5o.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_1_1_Plm.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_20_1_UdB.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_21_1_N5U.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_22_1_voU.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_23_1_QBs.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_24_1_xiB.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_25_1_pVI.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_26_1_FoL.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_27_1_n40.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_28_1_Sii.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_29_1_edl.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_2_1_guo.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_9_1_ath.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_30_1_1hO.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_8_1_3cL.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_31_1_WYj.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_7_1_eR0.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_32_1_IeV.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_6_1_NFn.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_33_1_wdn.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_5_1_6Lb.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_34_1_tAD.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_4_1_amr.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_35_1_ubn.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_46_1_tC8.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_36_1_GFW.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_45_1_SM0.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_37_1_1Tf.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_44_1_Vwe.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_38_1_yze.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_43_1_iel.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_39_1_s7v.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_42_1_XBo.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_3_1_77O.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_41_1_klR.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/HIJING_GEN-SIM_YUE-SHI_Minbias_v1/DPlusGun_HIJINGBkg_RECO_v1//f21bb6f86312349a22d6738f6ac34d23/reco_RAW2DIGI_L1Reco_RECO_40_1_k40.root'
#
		# Embedded data with small samples of either D or D0 both = 500 events
#	'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DReco/reco_RAW2DIGI_L1Reco_RECO.root'
#	'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/DReco/reco1_RAW2DIGI_L1Reco_RECO.root'
	
		# Real Data from CERN with 16570 events
#       '/store/hidata/HIRun2013A/PAHighPt/RECO/PromptReco-v1/000/210/634/FA4E6B7E-7366-E211-8DD0-0019B9F581C9.root'

		# Min Bias pPb Data 22 files at 12-70000 events per file/15 mil events.
       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_100_1_c24.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_101_1_J1s.root'
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_102_1_6zY.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_103_1_q4X.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_104_1_2Cx.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_105_1_7g3.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_106_1_E7o.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_107_1_OsP.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_108_1_Mcj.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_109_1_oof.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_10_1_ygj.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_110_1_8Wp.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_111_1_UoB.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_112_1_tc1.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_113_1_lvD.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_114_1_EAr.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_115_1_toX.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_116_1_KWG.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_117_1_UYs.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_118_1_dZ1.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_119_1_ahF.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_11_1_Leo.root',
#       'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v10/9bb5f96ac3303b1bd9a62a8991bd6aec/pPb_MB_120_1_jEn.root'	
	
		# MIT Skim data each one having ~50000 events
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_100_1_E8q.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_101_1_aaZ.root'
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_102_1_ZYH.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_10_2_Std.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_103_2_UZM.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_104_2_rvw.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_105_1_WMw.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_106_2_7i4.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_107_1_leQ.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_108_1_H8l.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_109_1_b1N.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_110_2_MMS.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_111_1_36c.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_11_1_SYW.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_112_2_FjG.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_113_2_wA8.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_114_2_gcU.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_115_2_Yrs.root',
#'root://xrootd1.cmsaf.mit.edu//store/user/davidlw/PAMinBiasUPC/PA2013_FlowCorr_PromptReco_MB_Gplus_v7/94df6300e56f6ebc7f3c427834e0dc6d/pPb_MB_116_1_h2I.root'	

	#Prompt Reco Data
#	'/store/hidata/HIRun2013/PAHighPt/RECO/PromptReco-v1/000/211/598/00000/D43483F1-2E74-E211-9216-003048D2BC38.root'
 )
)

process.demo = cms.EDAnalyzer('DAnalyzer'
  #  , tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
        , tracks = cms.untracked.InputTag('generalTracks')
        , vertices = cms.untracked.InputTag('offlinePrimaryVertices')
#	, verticesKal = cms.untracked.InputTag('offlinePrimaryVerticesKalman')
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo.root')
)

#process.p = cms.Path(process.demo)
process.p = cms.Path(process.hltHM*process.demo)
