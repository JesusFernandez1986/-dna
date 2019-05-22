import json

hair_color = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
facial_shape = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eye_color = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

eva = ["female", "white", "blonde", "blue", "oval"]
larisa = ["female", "white", "brown", "brown", "oval"]
mantej = ["male", "white", "black", "blue", "oval"]
miha = ["male", "white", "brown", "green", "square"]

with open("dna.txt" , "r") as dna_file:
    dna = dna_file.read()

caracteristicas = []

for x in eva:
    if x == "female":
        caracteristicas.append("TGAAGGACCTTC")
    elif x == "male":
        caracteristicas.append("TGCAGGAACTTC")
    elif x == "white":
        caracteristicas.append("AAAACCTCA")
    elif x == "black":
        caracteristicas.append("CGACTACAG")
    elif x == "asian":
        caracteristicas.append("CGCGGGCCG")
    elif x == "black":
        caracteristicas.append("CCAGCAATCGC")
    elif x == "brown":
        caracteristicas.append("GCCAGTGCCG")
    elif x ==  "blonde":
        caracteristicas.append("TTAGCTATCGC")
    elif x == "blue":
        caracteristicas.append("TTGTGGTGGC")
    elif x == "green":
        caracteristicas.append("GGGAGGTGGC")
    elif x == "brown":
        caracteristicas.append("AAGTAGTGAC")
    elif x == "square":
            caracteristicas.append("GCCACGG")
    elif x == "round":
        caracteristicas.append("ACCACAA")
    elif x == "oval":
        caracteristicas.append("AGGCCTCA")

dna_eva = str(caracteristicas[0])+str(caracteristicas[1])+str(caracteristicas[2]+str(caracteristicas[3])+str(caracteristicas[4]))
if dna_eva in dna:
    print("el culpable es eva")

for x in larisa:
    if x == "female":
        caracteristicas.append("TGAAGGACCTTC")
    elif x == "male":
        caracteristicas.append("TGCAGGAACTTC")
    elif x == "white":
        caracteristicas.append("AAAACCTCA")
    elif x == "black":
        caracteristicas.append("CGACTACAG")
    elif x == "asian":
        caracteristicas.append("CGCGGGCCG")
    elif x == "black":
        caracteristicas.append("CCAGCAATCGC")
    elif x == "brown":
        caracteristicas.append("GCCAGTGCCG")
    elif x ==  "blonde":
        caracteristicas.append("TTAGCTATCGC")
    elif x == "blue":
        caracteristicas.append("TTGTGGTGGC")
    elif x == "green":
        caracteristicas.append("GGGAGGTGGC")
    elif x == "brown":
        caracteristicas.append("AAGTAGTGAC")
    elif x == "square":
            caracteristicas.append("GCCACGG")
    elif x == "round":
        caracteristicas.append("ACCACAA")
    elif x == "oval":
        caracteristicas.append("AGGCCTCA")

dna_larisa = str(caracteristicas[0])+str(caracteristicas[1])+str(caracteristicas[2]+str(caracteristicas[3])+str(caracteristicas[4]))
if dna_larisa in dna:
    print("el culpable es larisa")

for x in mantej:
    if x == "female":
        caracteristicas.append("TGAAGGACCTTC")
    elif x == "male":
        caracteristicas.append("TGCAGGAACTTC")
    elif x == "white":
        caracteristicas.append("AAAACCTCA")
    elif x == "black":
        caracteristicas.append("CGACTACAG")
    elif x == "asian":
        caracteristicas.append("CGCGGGCCG")
    elif x == "black":
        caracteristicas.append("CCAGCAATCGC")
    elif x == "brown":
        caracteristicas.append("GCCAGTGCCG")
    elif x ==  "blonde":
        caracteristicas.append("TTAGCTATCGC")
    elif x == "blue":
        caracteristicas.append("TTGTGGTGGC")
    elif x == "green":
        caracteristicas.append("GGGAGGTGGC")
    elif x == "brown":
        caracteristicas.append("AAGTAGTGAC")
    elif x == "square":
            caracteristicas.append("GCCACGG")
    elif x == "round":
        caracteristicas.append("ACCACAA")
    elif x == "oval":
        caracteristicas.append("AGGCCTCA")

dna_mantej = str(caracteristicas[0])+str(caracteristicas[1])+str(caracteristicas[2]+str(caracteristicas[3])+str(caracteristicas[4]))
if dna_mantej in dna:
    print("el culpable es mantej")

for x in miha:
    if x == "female":
        caracteristicas.append("TGAAGGACCTTC")
    elif x == "male":
        caracteristicas.append("TGCAGGAACTTC")
    elif x == "white":
        caracteristicas.append("AAAACCTCA")
    elif x == "black":
        caracteristicas.append("CGACTACAG")
    elif x == "asian":
        caracteristicas.append("CGCGGGCCG")
    elif x == "black":
        caracteristicas.append("CCAGCAATCGC")
    elif x == "brown":
        caracteristicas.append("GCCAGTGCCG")
    elif x ==  "blonde":
        caracteristicas.append("TTAGCTATCGC")
    elif x == "blue":
        caracteristicas.append("TTGTGGTGGC")
    elif x == "green":
        caracteristicas.append("GGGAGGTGGC")
    elif x == "brown":
        caracteristicas.append("AAGTAGTGAC")
    elif x == "square":
            caracteristicas.append("GCCACGG")
    elif x == "round":
        caracteristicas.append("ACCACAA")
    elif x == "oval":
        caracteristicas.append("AGGCCTCA")
dna_miha = str(caracteristicas[0])+str(caracteristicas[1])+str(caracteristicas[2]+str(caracteristicas[3])+str(caracteristicas[4]))
print (dna_miha)
print(dna)
if dna_miha in dna:
    print("el culpable es miha")

