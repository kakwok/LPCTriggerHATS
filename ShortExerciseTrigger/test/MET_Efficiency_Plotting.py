import ROOT
import math 
import time
from plot_dict import *


file = ROOT.TFile("histos_METTrigNanoAOD.root")
workdir =file.GetDirectory("metTrigAnalyzerNanoAOD")


Numerator = workdir.Get("h_met_passtrig")
Denominator = workdir.Get("h_met_all")


Efficiency = ROOT.TGraphAsymmErrors(Numerator,Denominator,'MET')
Efficiency.SetLineColor(linecolor[1])
Efficiency.SetMarkerStyle(markerstylesolid[1])
Efficiency.SetMarkerColor(markercolor[1])
Efficiency.SetMarkerSize(1.5)
Efficiency.SetTitle("Trigger Efficiency")
Efficiency.GetXaxis().SetTitle("E_{T}^{miss} [GeV]")
Efficiency.GetYaxis().SetTitle("Efficiency of HLT_PFMET170")
Efficiency.GetYaxis().SetRange(0,2) 

legend = ROOT.TLegend(0.4412607,0.1932773,0.8223496,0.4453782)
legend.SetFillStyle(1001)
legend.SetBorderSize(0)
legend.AddEntry(Efficiency,"MET Trigger","ep")

canvas=ROOT.TCanvas("Trigger Efficiency", "Trigger Efficiency")
canvas.SetGrid()
Efficiency.Draw("ap")
legend.Draw("same")

canvas.SaveAs("eff_HLT_PFMET170_NanoAOD.png")
canvas.SaveAs("eff_HLT_PFMET170_NanoAOD.pdf")
