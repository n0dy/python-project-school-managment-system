from . import podaci as podaci
from . import glavni_meni as gmeni

def meni(ulogovan_profesor):
    global ulogovan
    ulogovan = ulogovan_profesor
    while True:
        try:
            meni_br = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n1. Dodavanje ocena studentu\n2. Brisanje ocene studentu\n3. Računanje prosečne ocene za predmet\n4. Promena termina konsultacija\n5. Povratak na glavni meni\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
            if(meni_br == 1):
                dodavanje_ocena()
            elif(meni_br == 2):
                brisanje_ocena()
            elif(meni_br == 3):
                prosecna_ocena()
            elif(meni_br == 4):
                promena_termina()
            elif(meni_br == 5):
                gmeni.meni()
            else:
                print("*Niste uneli postojeći broj, pokušajte ponovo!")
                continue
        except ValueError:
            print("*Niste uneli dobar tip podatka, pokušajte ponovo!")
            continue

def dodavanje_ocena():
    try:
        ime = input("-Unesite ime studenta: ")
        brojac = 0

        for x in podaci.studenti:
            if(x["ime"] == ime):
                brojac += 1
                print(brojac, ". ", x["br_indeksa"], " ", x["ime"], " ", x["prezime"])

        if(brojac == 0):
            print("*Nema studenata s tim imenom!")
            return
        
        broj_indeksa = int(input("-Unesite broj indeksa studenta: "))

        brojac = 0

        for x in podaci.studenti:
            if(x["br_indeksa"] == broj_indeksa):
                for y in podaci.predmeti:
                    pronadjeniStudenti = True
                    print(brojac, ". ", y["sifra"], " ", y["naziv"])
                    brojac += 1

                sifra_predmeta = int(input("-Unesite šifru predmeta: "))
                ocena = int(input("-Unesite ocenu: "))

                if(ocena < 5 or ocena > 10):
                    print("*Ocena mora biti u opsegu 5 - 10!")
                    return
                
                x["ocene"].append({"sifra_predmeta":sifra_predmeta, "sifra_profesora":ulogovan["sifra"], "ocena":ocena})
                podaci.cuvanje_podataka()
                print("|Ocena je uspešno dodata.")

        if(brojac == 0):
            print("*Nema studenata s tim indeksom!")

    except ValueError:
        print("*Niste uneli dobar tip podatka, pokušajte ponovo!")

def brisanje_ocena():
    try:
        ime = input("-Unesite ime studenta: ")
        brojac = 0

        for x in podaci.studenti:
            if(x["ime"] == ime):
                brojac += 1
                print(brojac, ". ", x["br_indeksa"], " ", x["ime"], " ", x["prezime"])
        
        if(brojac == 0):
            print("*Nema studenata s tim imenom!")
            return
        
        broj_indeksa = int(input("-Unesite broj indeksa studenta: "))
        brojac = 0
        pronadjenaOcena = False
        
        for x in podaci.studenti:
            if(x["br_indeksa"] == broj_indeksa):
                for y in x["ocene"]:
                    if(y["sifra_profesora"] == ulogovan["sifra"]):
                        pronadjenaOcena = True
                        print(brojac, ". ", y["sifra_predmeta"], " ", y["ocena"])
                        brojac += 1
                if(pronadjenaOcena == False):
                    print("*Student nema ocene!")
                    return

                try:
                    broj_ocene = int(input("-Unesite redni broj ocene: "))
                    x["ocene"].pop(broj_ocene)
                    podaci.cuvanje_podataka()
                    print("|Ocena je uspešno obrisana.")
                except IndexError:
                    print("*Greška!")

        if(brojac == 0):
            print("*Nema studenata s tim indeksom!")          

    except ValueError:
        print("*Niste uneli dobar tip podatka, pokušajte ponovo!")

def prosecna_ocena():
    brojac = 0
    for x in podaci.predmeti:
        print(brojac, ". ", x["sifra"], " ", x["naziv"])
        brojac += 1

    try:
        br_predmeta = int(input("-Unesite redni broj predmeta: "))
        suma = 0
        brojac = 0

        for x in podaci.studenti:
            for y in x["ocene"]:
                try:
                    if(podaci.predmeti[br_predmeta]["sifra"] == y["sifra_predmeta"]):
                        suma += y["ocena"]
                        brojac += 1
                except IndexError:
                    print("*Taj predmet nema ocena!")
                    return
        try:
            print("|Prosečna ocena je " + str(suma / brojac) + ".")
        except ZeroDivisionError:
            print("*Nemate prosečne ocene za taj predmet!")
    except ValueError:
        print("*Niste uneli dobar tip podatka, pokušajte ponovo!")

    

def promena_termina():
    try:
        dan = input("-Unesite dan u nedelji za promenu konsultacija: ")
        pocetak_vreme = int(input("-Od koliko sati: "))
        kraj_vreme = int(input("-Do koliko sati: "))

        for x in podaci.profesori:
            if(x["sifra"] == ulogovan["sifra"]):
                x["termin"] = dan
                x["vreme"] = str(pocetak_vreme) + "-" + str(kraj_vreme)
                podaci.cuvanje_podataka()
                print("|Uspešno je promenjen termin konsultacije.")

    except ValueError:
        print("*Niste uneli dobar tip podatka, pokušajte ponovo!")


    