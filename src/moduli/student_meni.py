from . import podaci as podaci
from . import glavni_meni as gmeni

def meni(ulogovan_korisnik):
    global ulogovan
    ulogovan = ulogovan_korisnik
    while True:
        try:
            meni_br = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n1. Računanje globalne prosečne cene\n2. Prikaz položenih ili nepoloženih predmeta po izboru studenta\n3. Prikaz podataka o profesoru koji predaje predmet\n4. Povratak na glavni meni\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
            if(meni_br == 1):
                prosecna_ocena()
            elif(meni_br == 2):
                prikaz_predmeta()
            elif(meni_br == 3):
                podaci_profesora()
            elif(meni_br == 4):
                gmeni.meni()
            else:
                print("*Niste uneli postojeći broj, pokušajte ponovo!")
                continue
        except ValueError:
            print("*Niste uneli dobar tip podatka, pokušajte ponovo!")
            continue

def prosecna_ocena():
    suma = 0
    br_ocena = 0

    for x in ulogovan["ocene"]:
        suma += x["ocena"]
        br_ocena += 1
    try:
        print("|Prosečna ocena je " + str(suma / br_ocena) + ".")
    except ZeroDivisionError:
        print("*Nemate ocene!")

def prikaz_predmeta():
    while True:
        try:
            meni_br = int(input("~~~~~~~~~~~~~~~~~~~~\n1. Položeni\n2. Nepoloženi\n~~~~~~~~~~~~~~~~~~~~\n"))
            br_predmeta = 0
            if(meni_br == 1):
                for x in podaci.predmeti:
                    for y in ulogovan["ocene"]:
                        if(y["sifra_predmeta"] == x["sifra"]):
                            print(x["naziv"])
                            br_predmeta += 1
                print("|Broj položenih predmeta je " + str(br_predmeta) + ".")
                break
            elif(meni_br == 2):
                for x in podaci.predmeti:
                    pronadjenPredmet = False
                    for y in ulogovan["ocene"]:
                        if(y["sifra_predmeta"] == x["sifra"]):
                            pronadjenPredmet = True
                    if pronadjenPredmet == False:
                        print(x["naziv"])
                        br_predmeta += 1
                print("|Broj nepoloženih predmeta je " + str(br_predmeta) + ".")          
                break          
            else:
                print("*Niste uneli postojeći broj, pokušajte ponovo!")
                continue
        except ValueError:
            print("*Niste uneli dobar tip podatka, pokušajte ponovo!")
            continue

def podaci_profesora():
    for x in podaci.predmeti:
        print(x["sifra"] , " " , x["naziv"])
    try:
        sifra = int(input("-Unesite sifru predmeta: "))
        br_pronadjenih = 0
        pronadjeni_profesori = []

        for x in podaci.studenti:
            for y in x["ocene"]:
                if y["sifra_predmeta"] == sifra:
                    pronadjen_profesor = False
                    for sif_profesora in pronadjeni_profesori:
                        if(sif_profesora == y["sifra_profesora"]):
                            pronadjen_profesor = True
                    if(pronadjen_profesor == False):
                        for z in podaci.profesori:
                            if y["sifra_profesora"] == z["sifra"]:
                                print("Email profesora: " + z["email"] + "\nIme i prezime: " + z["ime"] + " " + z["prezime"])
                                pronadjeni_profesori.append(y["sifra_profesora"])
                                br_pronadjenih += 1

        if(br_pronadjenih == 0):
            print("*Nijedan profesor ne predaje taj predmet!")

    except ValueError:
        print("*Niste uneli dobar tip podatka, pokušajte ponovo!")

