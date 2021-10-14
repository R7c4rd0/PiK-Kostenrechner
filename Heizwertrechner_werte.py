import pandas as pd
import argparse

Brennwerte = {"Mix": 2100, "Rotbuche":2100, "Eiche":2100, "Esche":2100, "Fichte": 1500, "Kiefer":1600, "Douglasie": 1700,"Birke":1900, "Pellets":4.8 }
Preise_1RM = {"Mix": 112.50, "Rotbuche":235, "Eiche":225, "Esche":229, "Fichte":0 , "Kiefer":0, "Douglasie":0 ,"Birke":219, "Pellets":0.23514 }
Preise_2RM = {"Mix": 305, "Rotbuche":339, "Eiche":319, "Esche":329, "Fichte":0 , "Kiefer":0, "Douglasie":0 ,"Birke":315, "Pellets":0.2214 }
Brenndauer = {"Mix": 2.5, "Rotbuche":2.5, "Eiche":2.5, "Esche":2.5, "Fichte":0 , "Kiefer":0, "Douglasie":0 , "Birke":1.5 }
Lieferpauschale = 40
MonatspreisÖL = 0.9039
pfad = "C:\\Users\\richa\\OneDrive\\Desktop\\"
print (pfad)

parser = argparse.ArgumentParser(description="Ausgabe der Kalkulationswerte für den Heizwertrechner")
parser.add_argument("-D","--Dateiformat", type = str, help = "zu nutzendes Format beim Speichern: .xlsx oder .csv")
parser.add_argument("-s","--abspeichern", required= False, type = str, help = "sollen die Kalkulationswerte in einer Datei abgespeichert werden: j/n")
parser.add_argument("-p","--pfad", type = str, help = "Orderpfad in welchem Datei abgelegt wird")

args = parser.parse_args() 


Spaltenindex ={ "Brennwerte": Brennwerte,  "Preise_1RM": Preise_1RM, "Preise_2RM": Preise_2RM, "Brenndauer": Brenndauer, }
Kalkulationswerte = pd.DataFrame(Spaltenindex)


# def kalkulationswerte (pfad = "C:\\Users\\richa\\OneDrive\\Desktop\\", Dateiformat =".csv", abspeichern = "j"):
#     print(Kalkulationswerte)
#     if abspeichern == "j":
#         if Dateiformat == ".csv":
#             Kalkulationswerte.to_csv( pfad +"Kalkulationswerte_Heizwertrechner.csv", sep= ";")
#         elif Dateiformat == ".xlsx":
#             Kalkulationswerte.to_excel(pfad +"Kalkulationswerte_Heizwertrechner.xlsx", )
#     elif abspeichern == "n":
#         pass
        
def kalkulationswerte (Dateiformat, abspeichern, pfad = "C:\\Users\\richa\\OneDrive\\Desktop\\"):
    # print(Kalkulationswerte)
    print(pfad)
    abspeichern = input("Möchten Sie die Kalkulationswerte abspeichern? j/n:  ")
    if abspeichern == "j":
        Dateiformat = input (".csv / .xlsx:   ")
        if Dateiformat == ".csv":
            Kalkulationswerte.to_csv( str(pfad) +"Kalkulationswerte_Heizwertrechner.csv", sep= ";")
        elif Dateiformat == ".xlsx":
            Kalkulationswerte.to_excel(str(pfad) +"Kalkulationswerte_Heizwertrechner.xlsx", )
        print("Die Datei Kalkulationswerte_Heizwertrechner" + str(Dateiformat) + " befindet sich in " + str(pfad))
    elif abspeichern == "n":
        print("\nDann halt nicht...")
    
if __name__ == "__main__":   
    print(kalkulationswerte(args.Dateiformat, args.abspeichern, args.pfad))
