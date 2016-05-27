from bs4 import BeautifulSoup


list= ["3KCol.xml",		"aba2096.xml",		"aha2749.xml",
"3rdFranRule.xml",		"aca1723.xml",		"aha6127.xml",
"AlphTales.xml"	,	"acb1675.xml",		"aha6129.xml",
"ArderneFistula.xml",	"acd9576.xml",		"ahb1325.xml",
"Blanchardyn.xml",		"acm9160.xml",		"ahb1341.xml",
"CharlesG.xml",		"acn1637.xml",		"ahb1378.xml",
"ChaucerAstr.xml",		"acs0188.xml",		"ahb1379.xml",
"ChaucerBo.xml",		"acv5981.xml",		"ajd3529.xml",
"Confessio.xml",		"acw2946.xml",		"ajd8171.xml",
"CookBk.xml",		"adq4048.xml",		"aje0623.xml",
"EEWills.xml",		"aeh6713.xml",		"ajf7399.xml",
"EGilds.xml",		"aew3422.xml",		"ajg4507.xml",
"EngConIre.xml",		"afb3713.xml",		"ajh1649.xml",
"GRom.xml",		"afw1075.xml",		"ajt2514.xml",
"HMaid.xml",		"afw1383.xml",		"ajt8111.xml",
"HarLyr.xml",		"afw5744.xml",		"ajt8124.xml",
"HenCres.xml",		"afy7793.xml",		"ajt8128.xml",
"HenFabl.xml",		"afy7823.xml",		"ajt8135.xml",
"HenMino.xml",		"afz9170.xml",		"alt5980.xml",
"HenOrpheus.xml",		"agd2855.xml",		"ant9911.xml",
"Juliana.xml",		"agv8488.xml",		"ant9912.xml",
"KntTour-L.xml",		"agz8232.xml",		"any9948.xml",
"LinDDoc.xml",		"agz8233.xml",		"anz2316.xml",
"LoveMirrour.xml",		"agz8234.xml",		"anz4356.xml",
"MaloryWks2.xml",		"agz8235.xml",		"anz4364.xml",
"Melusine.xml",		"agz8236.xml",		"apa1967.xml",
"Merlin.xml",		"agz8246.xml",		"ape7335.xml",
"Metham.xml",		"aha2626.xml",		"ape7380.xml",
"OctC.xml",		"aha2638.xml",		"ape9594.xml",
"OctL.xml",		"aha2639.xml",		"ape9595.xml",
"OwlC.xml",		"aha2659.xml",		"apg1531.xml",
"OwlJ.xml",		"aha2688.xml",		"ash2689.xml",
"PLAlex.xml",		"aha2700.xml",		"ash3725.xml",
"PPlCreed.xml",		"aha2702.xml",		"baa8159.xml",
"RatisRav.xml",		"aha2705.xml",		"bau0088.xml",
"RuleMinoresses.xml",	"aha2706.xml",		"bau1376.xml",
"RuleServLd.xml",		"aha2708.xml",		"deathjas.xml",
"SSecr.xml",		"aha2711.xml",		"lifesoul.xml",
"ThreeKSon.xml",		"aha2727.xml",		"rollecmp.xml",
"ThrnReligP.xml",		"aha2735.xml",		"rollewks.xml",
"Towneley.xml",		"aha2736.xml",		"tenwives.xml"]
"Vices+V1.xml",		"aha2738.xml",
"aaw7316.xml",		"aha2740.xml",

for x in range(0, len(list)):
	a= BeautifulSoup(open(list[x]));
	b=BeautifulSoup("<html>data</html>");
	c=a.find("title");
	q=list[x]+', ';
	d=c.string;
	print(q+repr(d));


