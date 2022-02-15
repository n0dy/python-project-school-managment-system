import csv
import json

studenti = []
predmeti = []
profesori = []

def cuvanje_podataka():
    cuvanje_studenata("data\studenti.json", studenti)
    cuvanje_profesora("data\profesori.csv", profesori)

def ucitavanje_podataka():
    global studenti
    global predmeti
    global profesori

    studenti = ucitavanje_studenata("data\studenti.json")
    predmeti = ucitavanje_predmeta("data\predmeti.csv")
    profesori = ucitavanje_profesora("data\profesori.csv")

def ucitavanje_predmeta(filename, delimiter_char = ';'):
    ucitani_predmeti = []
    try:
        with open(filename, 'r', encoding="utf-8") as fajl:
            predmeti_csv = csv.reader(fajl, delimiter=";")
            next(predmeti_csv)

            for x in predmeti_csv:
                ucitani_predmeti.append({"sifra":int(x[0]), "naziv":x[1]})
    except IOError as e:
        print("*Greška prilikom učitavanja predmeta!")
    except:
        print("*Greška prilikom učitavanja predmeta!")
    return ucitani_predmeti

def ucitavanje_profesora(filename):
    ucitani_profesori = []
    try:
        with open(filename, 'r', encoding="utf-8") as fajl:
            profesori_csv = csv.reader(fajl, delimiter=";")
            next(profesori_csv)

            for x in profesori_csv:
                ucitani_profesori.append({"sifra":int(x[0]), "lozinka":x[1], "ime":x[2], "prezime":x[3], "email":x[4], "termin":x[5], "vreme":x[6]})
    except IOError as e:
        print("*Greška prilikom učitavanja profesora!")
    except:
        print("*Greška prilikom učitavanja profesora!")
    return ucitani_profesori

def ucitavanje_studenata(filename):
    ucitani_studenti = []
    try:
        with open(filename, encoding='utf-8') as fajl:
            ucitani_studenti = json.load(fajl)
    except IOError as e:
        print("*Greška prilikom učitavanja studenata!")
    except:
        print("*Greška prilikom učitavanja studenata!")
    return ucitani_studenti

def cuvanje_studenata(filename, data):
    try:
        with open(filename, 'w', encoding="utf-8") as fajl:
            json.dump(data, fajl)
    except:
        print("*Greška prilikom čuvanja studenata!")
def cuvanje_profesora(filename, data):
    try:
        with open(filename, 'w', newline='', encoding="utf-8") as fajl:
            fieldnames = ['sifra', 'lozinka', 'ime', 'prezime', 'email', 'termin', 'vreme']
            writer = csv.DictWriter(fajl, fieldnames=fieldnames, delimiter=";")

            writer.writeheader()
            for x in data:
                writer.writerow(x)
    except:
        print("*Greška prilikom čuvanja profesora")