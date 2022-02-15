from . import podaci as podaci
from . import student_meni as smeni
from . import profesor_meni as pmeni

def meni():
    while True:
        try:
            meni_br = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n1. Prijava na sistem\n2. Registracija\n3. Izlazak iz aplikacije\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
            if(meni_br == 1):
                logovanje()
            elif(meni_br == 2):
                registracija()
            elif(meni_br == 3):
                exit()
            else:
                print("*Niste uneli postojeći broj, pokušajte ponovo!")
                continue
        except ValueError:
            print("*Niste uneli dobar tip podatka, pokušajte ponovo!")
            continue

def logovanje():
    try:
        id_korisnika = int(input("-Unesite broj indeksa ili šifru profesora: "))
        password_korisnika = input("-Unesite lozinku: ")

        for x in podaci.studenti:
            try:
                if x["br_indeksa"] == id_korisnika and x["lozinka"] == password_korisnika:
                    smeni.meni(x)
                    break
            except KeyError:
                break

        for x in podaci.profesori:
            try:
                if x["sifra"] == id_korisnika and x["lozinka"] == password_korisnika:
                    pmeni.meni(x)
                    break
            except KeyError:
                break

        print("*Neuspelo logovanje!")
    
    except ValueError:
        print("*Podaci koji ste uneli nisu u odgovarajućem formatu, pokušajte ponovo!")
def registracija():
    while True:
        try:
            meni_br = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n1. Registracija novog studenta\n2. Registracija novog profesora\n3. Povratak na glavni meni\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
            if(meni_br == 1):
                n_br_indeksa = int(input("-Unesite broj indeksa: "))
                n_lozinka = input("-Unesite lozinku: ")
                n_ime = input("-Unesite ime: ")
                n_prezime = input("-Unesite prezime: ")
                n_email = input("-Unesite email: ")

                pronadjen = False

                for x in podaci.studenti:
                    if x["br_indeksa"] == n_br_indeksa:
                        pronadjen = True

                for x in podaci.profesori:
                    if x["sifra"] == n_br_indeksa:
                        pronadjen = True

                if(pronadjen):
                    print("*Već postoji student ili profesor s tim indeksom ili korisničkim imenom!")
                else:
                    podaci.studenti.append({"br_indeksa":n_br_indeksa, "lozinka":n_lozinka, "ime":n_ime, "prezime":n_prezime, "email":n_email, "ocene":[]})
                    print("|Uspešno ste registrovali novog studenta.")
                    podaci.cuvanje_podataka()
                break
            elif(meni_br == 2):
                n_sifra = int(input("-Unesite šifru: "))
                n_lozinka = input("-Unesite lozinku: ")
                n_ime = input("-Unesite ime: ")
                n_prezime = input("-Unesite prezime: ")
                n_email = input("-Unesite email: ")
                n_termin = input("-Unesite dan termina: ")
                n_termin_od = int(input("-Unesite početak termina: "))
                n_termin_do = int(input("-Unesite kraj termina: "))

                pronadjen = False

                for x in podaci.profesori:
                    if x["sifra"] == n_sifra:
                        pronadjen = True

                for x in podaci.studenti:
                    if x["br_indeksa"] == n_sifra:
                        pronadjen = True

                if(pronadjen):
                    print("*Već postoji profesor ili student s tom šifrom ili tim korisničkim imenom!")
                else:
                    podaci.profesori.append({"sifra":n_sifra, "lozinka":n_lozinka, "ime":n_ime, "prezime":n_prezime, "email":n_email, "termin":n_termin, "vreme":str(n_termin_od) + "-" + str(n_termin_do)})
                    print("|Uspešno ste registrovali novog profesora.")
                    podaci.cuvanje_podataka()
                break
            elif(meni_br == 3):
                meni()
            else:
                print("*Niste uneli postojeći broj, pokušajte ponovo!")
                continue
        except ValueError:
            print("*Niste uneli dobar tip podatka, pokušajte ponovo!")
            continue