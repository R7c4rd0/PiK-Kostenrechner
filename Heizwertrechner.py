def fest_raum_meter (fm):
	raummeter = fm * 1.4
	return raummeter
def raum_fest_meter (rm):
	festmeter = rm * 1.4285

Brennwerte = {"Mix": 2100, "Rotbuche":2100, "Eiche":2100, "Esche":2100, "Fichte": 1500, "Kiefer":1600, "Douglasie": 1700,"Birke":1900, "Pellets":4.8 }
Preise_1RM = {"Mix": 112.50, "Rotbuche":235, "Eiche":225, "Esche":229, "Fichte":0 , "Kiefer":0, "Douglasie":0 ,"Birke":219, "Pellets":0.23514 }
Preise_2RM = {"Mix": 305, "Rotbuche":339, "Eiche":319, "Esche":329, "Fichte":0 , "Kiefer":0, "Douglasie":0 ,"Birke":315, "Pellets":0.2214 }
Brenndauer = {"Mix": 2.5, "Rotbuche":2.5, "Eiche":2.5, "Esche":2.5, "Fichte":0 , "Kiefer":0, "Douglasie":0 , "Birke":1.5 }
Lieferpauschale = 40
MonatspreisÖL = 0.9039
def heizwert (Holzart, Menge):
	Heizöl_l_Erdgas_m3 = (Brennwerte[Holzart] * Menge) / 10
	Heizwert = round(Brennwerte[Holzart]* 0.926 * Menge, 2)
	KostenHeizöl = round(Heizöl_l_Erdgas_m3 * MonatspreisÖL, 2)
	if Holzart == "Pellets":
		Kosten_xRM = Menge * 1000 * Preise_1RM[Holzart] + Lieferpauschale
		Kosten_EU_RM = round(Kosten_xRM / (Menge *1000) , 2) 
		EU_kwh = round(Kosten_EU_RM / Brennwerte[Holzart],2)
		Heizwert *= 1000
		Heizöl_l_Erdgas_m3 *= 1000
		KostenHeizöl = round(Heizöl_l_Erdgas_m3 * MonatspreisÖL,2)
		Ersparnis = (Heizöl_l_Erdgas_m3 * MonatspreisÖL) - Kosten_xRM
		return (str(Menge)+ "t "+ Holzart+" zum Preis von "+str(Kosten_xRM)+ " Euro bzw. "+ 
        		str(Kosten_EU_RM)+ " Euro/kg liefern "+str(Heizwert)+"kWh Heizwert und ersetzen "+ 
				str(Heizöl_l_Erdgas_m3)+ " l Heizöl (zum Preis von "+
				str(KostenHeizöl) + " €) bzw. "+ 
				str(Heizöl_l_Erdgas_m3)+" m³ Erdgas. Dies entspricht "+
				str(EU_kwh)+ " Euro/kWh."+ "Die Ersparnis im Vergleich zu Erdöl beträgt " + 
				str(round(Ersparnis))+ " €")

	if Menge % 2 == 0:
		Kosten_xRM = ((Menge * (Preise_2RM[Holzart]/2)))
		Kosten_EU_RM = Kosten_xRM / Menge
		EU_kwh = round(Kosten_EU_RM / Brennwerte[Holzart],2)
		Ersparnis = (Heizöl_l_Erdgas_m3 * MonatspreisÖL) - Kosten_xRM
		
	elif Menge % 2 !=0 :
		Kosten_xRM = ((Menge - 1) * (Preise_2RM[Holzart])/2) + Preise_1RM[Holzart]
		Kosten_EU_RM =  Kosten_xRM / Menge
		EU_kwh = round(Kosten_EU_RM / Brennwerte[Holzart],2)
		Ersparnis = (Heizöl_l_Erdgas_m3 * MonatspreisÖL) - Kosten_xRM 
	elif Menge == 1 or Menge < 1:
		Kosten_xRM = Preise_1RM[Holzart]
		Kosten_EU_RM = Preise_1RM[Holzart]
		EU_kwh = round(Kosten_EU_RM / Brennwerte[Holzart],2)
		Ersparnis = (Heizöl_l_Erdgas_m3 * MonatspreisÖL) - Kosten_xRM 
   
	return (str(Menge)+ " Raummeter "+ Holzart+
        	" zum Preis von "+str(Kosten_xRM)+ 
         	" Euro bzw. "+ str(Kosten_EU_RM)+ 
          	" Euro/Rm liefern "+str(Heizwert)+"kWh Heizwert und ersetzen "+ 
        	str(Heizöl_l_Erdgas_m3)+ " l Heizöl (zum Preis von "+
			str(KostenHeizöl) + " €) bzw. "+
        	str(Heizöl_l_Erdgas_m3)+
         	" m³ Erdgas. Dies entspricht "+str(EU_kwh)+ " Euro/kWh. "+ 
			"Die Ersparnis im Vergleich zu Erdöl beträgt " + str(round(Ersparnis))+ " €")


print(heizwert("Eiche",8)) 
