// -*- C++ -*-
//
// Package:    DAnalyzer
// Class:      DAnalyzer
// 
/**\class DAnalyzer DAnalyzer.cc Histo/DAnalyzer/src/DAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Michael Northup,,,
//         Created:  Fri Jul 19 01:04:02 CEST 2013
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TrackingTools/PatternTools/interface/ClosestApproachInRPhi.h"
#include "MagneticField/Engine/interface/MagneticField.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "CommonTools/CandUtils/interface/helicityAngle.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2D.h"
#include <Math/GenVector/PxPyPzE4D.h>
#include <Math/GenVector/PxPyPzM4D.h>
#include "DataFormats/Math/interface/Point3D.h"
#include "Math/Point3D.h"
#include "Math/GenVector/CoordinateSystemTags.h"
#include "TTree.h"
#include "TFile.h"

//
// class declaration
//

class DAnalyzer : public edm::EDAnalyzer {
   public:
      explicit DAnalyzer(const edm::ParameterSet&);
      ~DAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
      edm::InputTag trackTags_; //used to select what tracks to read from configuration file
      edm::InputTag vertexTags_;	
};
	TH1D * histoInvMassD0;
	TH1D * histoInvMassDplus;
	TH1D * histoPtD0;
	TH1D * histoPtDplus;
	TH1D * histoOpAngD0;
	TH1D * histoOpAngDplus;
	TH1D * histoEtaD0;
	TH1D * histoEtaDplus;
	TH1D * histochi2VertexD0;
	TH1D * histoVertErrxD0;
        TH1D * histoVertErryD0;
        TH1D * histoVertErrzD0;
	TH2D * histoVertXYD0;
	TH1D * histoVertzD0; 	
	TH1D * histoPointAngD0;
	TH1D * histoLxyMeasD0;	
	TH1D * histoPointAngxyD0;
	TH1D * histoLxySigD0;
	TH1D * histoDCAD0;
	TH1D * histoImParsigplusD0;
	TH1D * histoImParsigminD0;
	TH1D * histoImParplusD0;
	TH1D * histoImParminD0;
	TH1D * histoInvMassD0pair;
        TH1D * histoPtD0pair;
        TH1D * histochi2VertexD0pair;
        TH1D * histoPointAngD0pair;
        TH1D * histoLxyMeasD0pair;
        TH1D * histoPointAngxyD0pair;
	TH2D * histoPointAngchi2D0;
	TH2D * histoInvMassPtD0;
	TTree * tree;
	TBranch * branch;
	//TFile *f = new TFile("tree.root","RECREATE");
        //TTree * tree = new TTree("TestTree","Tree");

        struct str
        {
        double totpt;
	double vertexchi2;
	double vertposx;
	double vertposy;
	double vertposz;
	double PointAng;
	double PointAngxy;
	double Lxy;
	double Lxysig;
	double dpos;
	double dneg;
	double dpossig;
	double dnegsig;
	double InvMass;
        };
        str s;

        //TBranch * branch = tree->Branch("branch",&s,"a/I:b:c:d:e/D");
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DAnalyzer::DAnalyzer(const edm::ParameterSet& iConfig)
:
 trackTags_(iConfig.getUntrackedParameter<edm::InputTag>("tracks"))
, vertexTags_(iConfig.getUntrackedParameter<edm::InputTag>("vertices"))
{
   //now do what ever initialization is needed

	edm::Service<TFileService> fs;
	
	tree = fs->make<TTree>("DTree","Tree");
        branch = tree->Branch("D0",&s,"totpt/D:vertexchi2:vertposx:vertposy:vertposz:PointAng:PointAngxy:Lxy:Lxysig:dpos:dneg:dpossig:dnegsig:InvMass");

/*	histoInvMassD0 = fs->make<TH1D>("InvMassD0" , "Inv Mass D0", 100 ,1.75,2.0);
        histoInvMassDplus = fs->make<TH1D>("InvMassDplus","Inv Mass Dplus", 60, 1.70, 1.95);
        histoPtD0 = fs->make<TH1D>("PtD0","Pt D0", 200, 0.0, 100.0);
        histoPtDplus = fs->make<TH1D>("PtDplus","Pt Dplus", 100, 0.0, 5.0);
        histoOpAngD0 = fs->make<TH1D>("OpAngD0","Op Ang D0", 100, 0.0, 3.2);
        histoOpAngDplus = fs->make<TH1D>("OpAngDplus","Op Ang Dplus", 100, 0.0, 3.2);
        histoEtaD0 = fs->make<TH1D>("EtaD0","Eta D0", 200, -3.0, 3.0);
        histoEtaDplus = fs->make<TH1D>("EtaDlus","Eta Dplus", 200, -3.0, 3.0);
	histochi2VertexD0 = fs->make<TH1D>("chi2VertexD0","Chi2 for Fit Vertices D0",100, 0.0, 5.0);
        histoVertErrxD0 = fs->make<TH1D>("VertErrxD0","Error for x pos of Fit Vertices D0",100, 0.0, 10.0);
        histoVertErryD0 = fs->make<TH1D>("VertErryD0","Error for y pos of Fit Vertices D0",100, 0.0, 10.0);
        histoVertErrzD0 = fs->make<TH1D>("VertErrzD0","Error for z pos of Fit Vertices D0",100, 0.0, 10.0);
	histoVertXYD0 = fs->make<TH2D>("VertXYD0","Position of D0 Vertices in X-Y Plain", 100, -5.0, 5.0, 100, -5.0, 5.0);	
        histoVertzD0 = fs->make<TH1D>("VertzD0","Position of D0 Vertices in z", 300, -10.0, 10.0);
        histoPointAngD0 = fs->make<TH1D>("PointAngD0","pointing angle for D0", 100,-0.2, 3.2);
	histoLxyMeasD0 = fs->make<TH1D>("LxyMeasD0","Measured Lxy for D0",500,0.0,5.0);
	histoPointAngxyD0 = fs->make<TH1D>("PointAngxyD0","point Angle in the xy plain",100,-0.2,3.2);
	histoLxySigD0 = fs->make<TH1D>("LxySig","Sig of Lxy D0",100,0.0,50.0);
	histoImParplusD0 = fs->make<TH1D>("ImParplusD0","Imp Param for plus track D0",100,0.0,1.0);
        histoImParminD0 = fs->make<TH1D>("ImParminD0","Imp Param for minus track D0",100,0.0,1.0);
	histoInvMassD0pair = fs->make<TH1D>("histoInvMassD0pair","Inv Mass oF D0 pair",100,1.75,2.0);
        histoPtD0pair = fs->make<TH1D>("ptD0pair","pt D0 pair",100,10.0,30.0);
        histochi2VertexD0pair = fs->make<TH1D>("chi2D0pair","chi2 D0 pair",100,0.0,5.0);
        histoPointAngD0pair = fs->make<TH1D>("cosPointAngxyD0pair","cos of point Angle pair",100,-1.2,1.2);
        histoLxyMeasD0pair = fs->make<TH1D>("LxyMeasD0pair","Lxy Meas D0 pair",500,0.0,5.0);
        histoPointAngxyD0pair = fs->make<TH1D>("cosPointAngxyD0pair","cos of point Angle in the xy plain pair",100,-1.2,1.2); 
	histoPointAngchi2D0 = fs->make<TH2D>("PointAngchi2D0","chi2 vs. pointing angle for D0",100,-0.2,3.14159,100,0,5.0);
	histoInvMassPtD0 = fs->make<TH2D>("InvMassPtD0","Pt vs. Inv Mass for D0",100,1.70,2.00,100,0.0,30.0); 
	histoDCAD0 = fs->make<TH1D>("DCAD0","Dist of clos approach for D0",250,0.0,10.0);
        histoImParsigplusD0 = fs->make<TH1D>("ImParsigplusD0","Significance of Impact Parameter for plus charge D0 candidates",100,0.0,50.0);
        histoImParsigminD0 = fs->make<TH1D>("ImParsigminD0","Significance of Impact Parameter for minus charge D0 candidates",100,0.0,50.0);*/
}


DAnalyzer::~DAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;
   using namespace reco;
   using namespace math;
   //using reco::TrackCollection;
   //using reco::TransientTrack;
  
   double mpi = 0.1396; 
   double mK = 	0.4937;	
   double track1px = 0.0;
   double track1py = 0.0;
   double track1pz = 0.0;
   double track1E = 0.0;
   double track1p = 0.0;
   double track2px = 0.0;
   double track2py = 0.0;
   double track2pz = 0.0;
   double track2E = 0.0;
   double track2p = 0.0;
   double tracktotp = 0.0;
   double tracktotpt = 0.0;
   double tracktotpx = 0.0;
   double tracktotpy = 0.0;
   double tracktotpz = 0.0;
   double tracktotE = 0.0;
   double InvMassD0 = 0.0;
   double vertTrackOld = 0.0;
   double vertTrackNew = 0.0;
   double vertPrimPosx = 0.0;
   double vertPrimPosy = 0.0;
   double vertPrimPosz = 0.0;
   double decaylengthx = 0.0;
   double decaylengthy = 0.0;           
   double decaylengthz = 0.0;           
   double decaylength = 0.0;           
   double PointAngD0 = 0.0;
   double PointAngxyD0 = 0.0;
   double LxyCalD0 = 0.0;
   double LxyMeasD0 = 0.0;
   double ctauD0 = 1.23*pow(10,-4);
   double ctauDplus = 3.12*pow(10,-4);
   double mD0 = 1.8649;
   double mDplus = 1.8697;
   double decaylengthtrans = 0.0;

   double ptTol = 1.0;
   double Lxysigtol = 5.0;
   double PointAngD0tol = 0.3;
   double dcatol = 0.1;
   double d0plussigtol = 1.0;
   double d0minsigtol = 1.0;

   double dxy1 = 0.0;
   double dxy2 = 0.0;
   double dz1 = 0.0;
   double dz2 = 0.0;
   double d01 = 0.0;
   double d02 = 0.0;
   double dxy1err = 0.0;
   double dxy2err = 0.0;
   double dz1err = 0.0;
   double dz2err = 0.0;
   double derr1 = 0.0;
   double derr2 = 0.0;
   double sig1 = 0.0;
   double sig2 = 0.0;
   double primverterrx = 0.0;
   double primverterry = 0.0;
   double primverterrz = 0.0;
   double secverterrx = 0.0;
   double secverterry = 0.0;
   double secverterrz = 0.0;
   double Lxyerr = 0.0;
   double Lxysig = 0.0;
   double hang = 0.0;
   double dca = 0.0;
   Vertex pv; 
   FreeTrajectoryState posState; 
   FreeTrajectoryState negState; 

	
   Handle<VertexCollection> vertices;
   iEvent.getByLabel(vertexTags_, vertices); 
   Handle<TrackCollection> tracks;
   iEvent.getByLabel(trackTags_,tracks);
    //get the builder:
   ESHandle<TransientTrackBuilder> theB;
   iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",theB);
   //do the conversion:
   vector<TransientTrack> ttracks = (*theB).build(tracks);
   vector<TransientTrack> ttracksv;
   KalmanVertexFitter fitter;

	for(VertexCollection::const_iterator itVertex = vertices->begin(); itVertex != vertices->end(); ++itVertex)              
   	{                                    
        vertTrackNew = itVertex->tracksSize();
        if (vertTrackNew > vertTrackOld)
        	{                               
                	vertPrimPosx = itVertex->x();
                	vertPrimPosy = itVertex->y();
                	vertPrimPosz = itVertex->z();
			pv = (*itVertex);
			vertTrackOld = vertTrackNew;    
        	}                                       
  	}                                 
//	vertPrimPosx = 0.0;
//	vertPrimPosy = 0.0;
//	vertPrimPosz = 0.0;
        XYZPoint PrimVert = {vertPrimPosx,vertPrimPosy,vertPrimPosz};
 	
 	//Here's where we cycle over all pairs of transient tracks
	for (unsigned int i = 0; i < ttracks.size(); i++)
	{
		for (unsigned int j = 0; j < ttracks.size(); j++)
		{	
		TransientTrack t1 = ttracks.at(i);
		TransientTrack t2 = ttracks.at(j);
	
			if (t1.charge() == 1.0 && t2.charge() == -1.0)
			{
			        posState = t1.impactPointTSCP().theState();
		                negState = t2.impactPointTSCP().theState();
				 
				if( !t1.impactPointTSCP().isValid() || !t2.impactPointTSCP().isValid() ) continue;

       				// Measure distance between tracks at their closest approach
       				ClosestApproachInRPhi cApp;
       				cApp.calculate(posState, negState);
       				if( !cApp.status() ) continue;
       				dca = fabs( cApp.distance() );
       				//GlobalPoint cxPt = cApp.crossingPoint();
				if (dca < 0.0 || dca > dcatol) continue;			
	
				track1px = t1.track().px();
                        	track1py = t1.track().py();
                        	track1pz = t1.track().pz();
                        	track2px = t2.track().px();
                        	track2py = t2.track().py();
                        	track2pz = t2.track().pz();
                        	track1p = sqrt(track1px*track1px + track1py*track1py + track1pz*track1pz);                                    
                        	track2p = sqrt(track2px*track2px + track2py*track2py + track2pz*track2pz);
                        	track1E = sqrt(track1p*track1p + mpi*mpi);
                        	track2E = sqrt(track2p*track2p + mK*mK);
                        	tracktotpx = track1px + track2px;
                        	tracktotpy = track1py + track2py;
                        	tracktotpz = track1pz + track2pz;
                        	tracktotp = sqrt(tracktotpx*tracktotpx + tracktotpy*tracktotpy + tracktotpz*tracktotpz);
                        	tracktotE = track1E + track2E;
                        	InvMassD0 = sqrt(tracktotE*tracktotE - tracktotp*tracktotp);
                                tracktotpt = sqrt(tracktotpx*tracktotpx + tracktotpy*tracktotpy);
				dxy1 = t1.track().dxy(PrimVert);
                                dxy2 = t2.track().dxy(PrimVert);
				dz1 = t1.track().dz(PrimVert);
				dz2 = t2.track().dz(PrimVert);
				d01 = sqrt(dxy1*dxy1 + dz1*dz1);
				d02 = sqrt(dxy2*dxy2 + dz2*dz2);
				dxy1err = t1.track().dxyError();
				dxy2err = t2.track().dxyError();
				dz1err = t1.track().dzError();
				dz2err = t2.track().dzError();
				derr1 = sqrt(dxy1err*dxy1err + dz1err*dz1err);
				derr2 = sqrt(dxy2err*dxy2err + dz2err*dz2err);
				sig1 = fabs(d01)/derr1;
				sig2 = fabs(d02)/derr2;

				ttracksv = {t1,t2};
				if ((tracktotpt > ptTol)/* && (t1.track().chi2() < 1.0) && (t1.track().chi2() < 1.0)*/ && (sig1 > d0plussigtol) && (sig2 > d0minsigtol))
				{	
					TransientVertex tvertex = fitter.vertex(ttracksv);
					
					if (tvertex.isValid())
					{
						decaylengthx = tvertex.position().x() - vertPrimPosx;
                                                decaylengthy = tvertex.position().y() - vertPrimPosy;
                                                decaylengthz = tvertex.position().z() - vertPrimPosz;
						decaylength = sqrt(decaylengthx*decaylengthx + decaylengthy*decaylengthy + decaylengthz*decaylengthz);
                                                LxyCalD0 = ctauD0*tracktotpt/mD0;
                                                LxyMeasD0 = sqrt(decaylengthx*decaylengthx + decaylengthy*decaylengthy);	
						PointAngxyD0 = acos((tracktotpx*decaylengthx + tracktotpy*decaylengthy)/(tracktotpt*LxyMeasD0));
                                                PointAngD0 = acos((tracktotpx*decaylengthx + tracktotpy*decaylengthy  + tracktotpz*decaylengthz)/(tracktotp*decaylength));
					//	cout << decaylengthx << " " << decaylengthy << " " << decaylengthz << " " << tracktotpx << " " << tracktotpy << " " <<
					//		tracktotpz << " " <<  decaylength << " " << tracktotp << " " << tracktotpt << " " << PointAngD0 << " " <<
					//		PointAngxyD0 << endl;
 
						primverterrx = pv.xError();				
						primverterry = pv.yError();
						primverterrz = pv.zError();
						secverterrx = tvertex.positionError().cxx();
						secverterry = tvertex.positionError().cyy();
						secverterrz = tvertex.positionError().czz();
						Lxyerr = sqrt(primverterrx*primverterrx + primverterry*primverterry + secverterrx*secverterrx + 								secverterry*secverterry);
						Lxysig = LxyMeasD0/Lxyerr;
						if ((Lxysig > Lxysigtol) && (PointAngD0 < PointAngD0tol))
						{
					/*	histoInvMassD0->Fill(InvMassD0);
						histoPtD0->Fill(tracktotpt);
						histochi2VertexD0->Fill(tvertex.totalChiSquared());
						histoVertXYD0->Fill(tvertex.position().x(), tvertex.position().y());
						histoVertzD0->Fill(tvertex.position().z());
						histoPointAngxyD0->Fill(PointAngxyD0);
						histoPointAngD0->Fill(PointAngD0);
                                                histoLxyMeasD0->Fill(LxyMeasD0);
						histoLxySigD0->Fill(Lxysig);
						histoImParplusD0->Fill(d01);
						histoImParminD0->Fill(d02); 
						histoImParsigplusD0->Fill(sig1);
						histoImParsigminD0->Fill(sig2);
						histoDCAD0->Fill(dca);
						histoPointAngchi2D0->Fill(PointAngD0,tvertex.totalChiSquared());
						histoInvMassPtD0->Fill(InvMassD0,tracktotpt);
					*/
						s.totpt = tracktotpt;
        					s.vertexchi2 = tvertex.totalChiSquared();
        					s.vertposx = tvertex.position().x();
        					s.vertposy = tvertex.position().y();
						s.vertposz = tvertex.position().z();
						s.PointAng = PointAngD0;
        					s.PointAngxy = PointAngxyD0;
        					s.Lxy = LxyMeasD0;
        					s.Lxysig = Lxysig;
        					s.dpos = d01;
        					s.dneg = d02;
        					s.dpossig = sig1;
       						s.dnegsig = sig2;
					        s.InvMass = InvMassD0;
	
						tree->Fill();
						}
					}
				}
			}  
			else if (t1.charge() == -1.0 && t2.charge() == 1.0)
                        {
				posState = t2.impactPointTSCP().theState();
                                negState = t1.impactPointTSCP().theState();
                                 
                                if( !t1.impactPointTSCP().isValid() || !t2.impactPointTSCP().isValid() ) continue;
                                
                                // Measure distance between tracks at their closest approach
                                ClosestApproachInRPhi cApp;
                                cApp.calculate(posState, negState);
                                if( !cApp.status() ) continue;
                                dca = fabs( cApp.distance() );
                                //GlobalPoint cxPt = cApp.crossingPoint();
                                if (dca < 0.0 || dca > dcatol) continue;

				track1px = t1.track().px();
                                track1py = t1.track().py();
                                track1pz = t1.track().pz();
                                track2px = t2.track().px();
                                track2py = t2.track().py();
                                track2pz = t2.track().pz();
                                track1p = sqrt(track1px*track1px + track1py*track1py + track1pz*track1pz);
                                track2p = sqrt(track2px*track2px + track2py*track2py + track2pz*track2pz);
                                track1E = sqrt(track1p*track1p + mK*mK);
                                track2E = sqrt(track2p*track2p + mpi*mpi);
                                tracktotpx = track1px + track2px;
                                tracktotpy = track1py + track2py;
                                tracktotpz = track1pz + track2pz;
                                tracktotp = sqrt(tracktotpx*tracktotpx + tracktotpy*tracktotpy + tracktotpz*tracktotpz);
                                tracktotE = track1E + track2E;
                                InvMassD0 = sqrt(tracktotE*tracktotE - tracktotp*tracktotp);
                                tracktotpt = sqrt(tracktotpx*tracktotpx + tracktotpy*tracktotpy);
				dxy1 = t1.track().dxy(PrimVert);
                                dxy2 = t2.track().dxy(PrimVert);
                                dz1 = t1.track().dz(PrimVert);
                                dz2 = t2.track().dz(PrimVert);
                                d01 = sqrt(dxy1*dxy1 + dz1*dz1);
                                d02 = sqrt(dxy2*dxy2 + dz2*dz2);
                                dxy1err = t1.track().dxyError();
                                dxy2err = t2.track().dxyError();
                                dz1err = t1.track().dzError();
                                dz2err = t2.track().dzError();
                                derr1 = sqrt(dxy1err*dxy1err + dz1err*dz1err);
                                derr2 = sqrt(dxy2err*dxy2err + dz2err*dz2err);
                                sig1 = fabs(d01)/derr1;
                                sig2 = fabs(d02)/derr2;

                                ttracksv = {t1,t2};
                                if (tracktotpt > ptTol/* && (t1.track().chi2() < 1.0) && (t1.track().chi2() < 1.0)*/ && (sig2 > d0plussigtol) && (sig1 > d0minsigtol))
                                {
					TransientVertex tvertex = fitter.vertex(ttracksv);

                                        if (tvertex.isValid())
                                        {
						decaylengthx = tvertex.position().x() - vertPrimPosx;
                                                decaylengthy = tvertex.position().y() - vertPrimPosy;
                                                decaylengthz = tvertex.position().z() - vertPrimPosz;
                                                decaylength = sqrt(decaylengthx*decaylengthx + decaylengthy*decaylengthy + decaylengthz*decaylengthz);
                                                LxyCalD0 = ctauD0*tracktotpt/mD0;
                                                LxyMeasD0 = sqrt(decaylengthx*decaylengthx + decaylengthy*decaylengthy);
                                                PointAngxyD0 = acos((tracktotpx*decaylengthx + tracktotpy*decaylengthy)/(tracktotpt*LxyMeasD0));
                                                PointAngD0 = acos((tracktotpx*decaylengthx + tracktotpy*decaylengthy  + tracktotpz*decaylengthz)/(tracktotp*decaylength));
                                                primverterrx = pv.xError();
                                                primverterry = pv.yError();
                                                primverterrz = pv.zError();
                                                secverterrx = tvertex.positionError().cxx();
                                                secverterry = tvertex.positionError().cyy();
                                                secverterrz = tvertex.positionError().czz();
                                                Lxyerr = sqrt(primverterrx*primverterrx + primverterry*primverterry  + secverterrx*secverterrx +                                                             secverterry*secverterry);
                                                Lxysig = LxyMeasD0/Lxyerr;

                                                if ((Lxysig > Lxysigtol) && (PointAngD0 < PointAngD0tol))
						{
						
					/*	histoInvMassD0->Fill(InvMassD0);
                                                histoPtD0->Fill(tracktotpt);
                                                histochi2VertexD0->Fill(tvertex.totalChiSquared());
                                                histoVertXYD0->Fill(tvertex.position().x(), tvertex.position().y());
                                                histoVertzD0->Fill(tvertex.position().z());
                                                histoPointAngxyD0->Fill(PointAngxyD0);
						histoPointAngD0->Fill(PointAngD0);
                                                histoLxyMeasD0->Fill(LxyMeasD0);
						histoLxySigD0->Fill(Lxysig);
                                                histoImParsigplusD0->Fill(sig2);
                                                histoImParsigminD0->Fill(sig1);
                                                histoDCAD0->Fill(dca);
 						histoImParplusD0->Fill(d02);
                                                histoImParminD0->Fill(d01);
                                                histoPointAngchi2D0->Fill(PointAngD0,tvertex.totalChiSquared());
						histoInvMassPtD0->Fill(InvMassD0,tracktotpt);
                                          */      
						s.totpt = tracktotpt;
                                                s.vertexchi2 = tvertex.totalChiSquared();
                                                s.vertposx = tvertex.position().x();
                                                s.vertposy = tvertex.position().y();
                                                s.vertposz = tvertex.position().z();
                                                s.PointAng = PointAngD0;
                                                s.PointAngxy = PointAngxyD0;
                                                s.Lxy = LxyMeasD0;
                                                s.Lxysig = Lxysig;
                                                s.dpos = d02;
                                                s.dneg = d01;
                                                s.dpossig = sig2;
                                                s.dnegsig = sig1;
                                                s.InvMass = InvMassD0;
	
						tree->Fill();
                                        	}
					}
                                }
                        }

		}
	}   

/*  for(TrackCollection::const_iterator itTrack = tracks->begin(); itTrack != tracks->end(); ++itTrack) 
	{        
	for(TrackCollection::const_iterator itTrack2 = tracks->begin(); itTrack2 != tracks->end(); ++itTrack2)
		{
			if ((itTrack->charge() == 1) && (itTrack2->charge() == -1))
			{
							
				track1px = itTrack->px();
				track1py = itTrack->py();
				track1pz = itTrack->pz();
				track2px = itTrack2->px();
				track2py = itTrack2->py();
				track2pz = itTrack2->pz();
				track1p = sqrt(pow(track1px,2) + pow(track1py,2) + pow(track1pz,2));				 	
                                track2p = sqrt(pow(track2px,2) + pow(track2py,2) + pow(track2pz,2));
				track1E = sqrt(pow(track1p,2) + pow(mpi,2));
                                track2E = sqrt(pow(track2p,2) + pow(mK,2));
				tracktotpx = track1px + track2px;
                                tracktotpy = track1py + track2py;
                                tracktotpz = track1pz + track2pz;
				tracktotp = sqrt(pow(tracktotpx,2) + pow(tracktotpy,2) + pow(tracktotpz,2));
				tracktotE = track1E + track2E;
				InvMassD0 = sqrt(pow(tracktotE,2) - pow(tracktotp,2));
                                tracktotpt = sqrt(pow(tracktotpx,2) + pow(tracktotpy,2));
			
				decaylengthx = tvertex.x() - vertPrimPosx;
                                decaylengthy = tvertex.position().y() - vertPrimPosy;
                                decaylengthz = tvertex.position().z() - vertPrimPosz;
                                decaylength = sqrt(pow(decaylengthx,2) + pow(decaylengthy,2) + pow(decaylengthz,2));
                                cosPointAngxyD0 = (tracktotpx*decaylengthx + tracktotpy*decaylengthy)/(tracktotpt*decaylength);
                                cosPointAngD0 = (tracktotpx*decaylengthx + tracktotpy*decaylengthy  + tracktotpz*decaylengthz)/(tracktotp*decaylength);
                                LxyCalD0 = ctauD0*tracktotpt/mD0;
                                LxyMeasD0 = sqrt(pow(decaylengthx,2) + pow(decaylengthy,2));			
				
				if (tracktotpt > ptTol)
				{
					histoInvMassD0pair->Fill(InvMassD0);
					histoPtD0pair->Fill(tracktotpt);
                                        //histochi2VertexD0pair->Fill(;
                                        //histocosPointAngD0pair;
                                        //histoLxyMeasD0pair;
                                        //histocosPointAngxyD0pair;
				}
			}
			else if ((itTrack->charge() == -1) && (itTrack2->charge() == 1))
			{
			        track1px = itTrack->px();
                                track1py = itTrack->py();
                                track1pz = itTrack->pz();
                                track2px = itTrack2->px();
                                track2py = itTrack2->py();
                                track2pz = itTrack2->pz();
                                track1p = sqrt(pow(track1px,2) + pow(track1py,2) + pow(track1pz,2));
                                track2p = sqrt(pow(track2px,2) + pow(track2py,2) + pow(track2pz,2));
                                track1E = sqrt(pow(track1p,2) + pow(mK,2));
                                track2E = sqrt(pow(track2p,2) + pow(mpi,2));
                                tracktotpx = track1px + track2px;
                                tracktotpy = track1py + track2py;
                                tracktotpz = track1pz + track2pz;
                                tracktotp = sqrt(pow(tracktotpx,2) + pow(tracktotpy,2) + pow(tracktotpz,2));
                                tracktotE = track1E + track2E;
                                InvMassD0 = sqrt(pow(tracktotE,2) - pow(tracktotp,2));
				tracktotpt = sqrt(pow(tracktotpx,2) + pow(tracktotpy,2));
				
				if (tracktotpt > ptTol)
				{
					histoPtD0pair->Fill(tracktotpt);
                                	histoInvMassD0pair->Fill(InvMassD0);
				}
			}
		} 
	}*/ 	 

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
DAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DAnalyzer::endJob() 
{
	//f->Close();
}

// ------------ method called when starting to processes a run  ------------
void 
DAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

 //Specify that only 'tracks' is allowed
 //To use, remove the default given above and uncomment below
 //ParameterSetDescription desc;
 //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
 //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DAnalyzer);
