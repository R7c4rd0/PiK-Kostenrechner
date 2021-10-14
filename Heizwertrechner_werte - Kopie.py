import pandas as pd
import argparse
import colorama

colorama.init()

Brennwerte = {"Mix": 2100, "Rotbuche":2100, "Eiche":2100, "Esche":2100, "Fichte": 1500, "Kiefer":1600, "Douglasie": 1700,"Birke":1900, "Pellets":4.8 }
Preise_1RM = {"Mix": 112.50, "Rotbuche":235, "Eiche":225, "Esche":229, "Fichte":0 , "Kiefer":0, "Douglasie":0 ,"Birke":219, "Pellets":0.23514 }
Preise_2RM = {"Mix": 305, "Rotbuche":339, "Eiche":319, "Esche":329, "Fichte":0 , "Kiefer":0, "Douglasie":0 ,"Birke":315, "Pellets":0.2214 }
Brenndauer = {"Mix": 2.5, "Rotbuche":2.5, "Eiche":2.5, "Esche":2.5, "Fichte":0 , "Kiefer":0, "Douglasie":0 , "Birke":1.5 }
Lieferpauschale = 40
MonatspreisÖL = 0.9039
pfad = "C:\\Users\\richa\\OneDrive\\Desktop\\"




Spaltenindex ={ "Brennwerte": Brennwerte,  "Preise_1RM": Preise_1RM, "Preise_2RM": Preise_2RM, "Brenndauer": Brenndauer, }
Kalkulationswerte = pd.DataFrame(Spaltenindex)


        
def kalkulationswerte (Dateiformat = ".xlsx", abspeichern = "j", pfad = "C:\\Users\\richa\\OneDrive\\Desktop\\"):
    print(Kalkulationswerte)
    abspeichern = input( colorama.Fore.CYAN +"\nMöchten Sie die Kalkulationswerte abspeichern? j/n:  ")
    if abspeichern == "j":
        Dateiformat = input ( colorama.Fore.CYAN +"\nDie Tabelle wird als .xlsx gespeichert. Abspeichern als .csv?\nj/n:  ")
        if Dateiformat == "j":
            Kalkulationswerte.to_csv( str(pfad) +"Kalkulationswerte_Heizwertrechner.csv", sep= ";")
            return colorama.Fore.GREEN +"\nDie Datei Kalkulationswerte_Heizwertrechner.csv befindet sich in " + str(pfad)
        else:
            Kalkulationswerte.to_excel(str(pfad) +"Kalkulationswerte_Heizwertrechner.xlsx", )
            return colorama.Fore.GREEN +"\nDie Datei Kalkulationswerte_Heizwertrechner.xlsx befindet sich in " + str(pfad)+"\n"
    elif abspeichern == "n":
        return colorama.Fore.YELLOW +"\nDann halt nicht...\n"
    
if __name__ == "__main__":   
    print(kalkulationswerte())

colorama.deinit()