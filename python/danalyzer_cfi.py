import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('DAnalyzer'
    ,tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
)
