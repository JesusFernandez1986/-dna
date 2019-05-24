imero creamos varios diccionarios con las posibles variantes de cada caracteristica
hair_color = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
facial_shape = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eye_color = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

#creamos 4 listas para cada uno de los sospechosos con sus caracteristicas
eva = ["female", "white", "blonde", "blue", "oval"]
larisa = ["female", "white", "brown", "brown", "oval"]
mantej = ["male", "white", "black", "blue", "oval"]
miha = ["male", "white", "brown", "green", "square"]

#abrimos el archivo dna.txt en modo lectura y guardamos su valor en la variable dna
with open("dna.txt" , "r") as dna_file:
    dna = dna_file.read()
#creamos una nueva lista llamada caracteristicas
caracteristicas = []

#hacemos un bucle que recorra la lista de cada uno de los sospechosos y vaya añadiendo a la lista caracteristicas
#los valors que concidan
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
#creamos una variable nueva en la que todos los valores que tiene caracteristicas sean concatenados
dna_eva = str(caracteristicas[0])+str(caracteristicas[1])+str(caracteristicas[2]+str(caracteristicas[3])+str(caracteristicas[4]))
# comparamos si la concatenacion de la variable de eva esta dentro de la variable dna y en caso de ser afirmativo imprima un
# mensaje diciendo que es el culpable
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
if dna_miha in dna:
    print("el culpable es mantej")
# otra manera de comprobar si la variable dna_miha esta incluida en la variable dna
if dna.find(dna_miha) >= 0:
	print("el culpable es miha")


