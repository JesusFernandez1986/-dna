characteristics ={"hair color" :["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"],
"facial_shape": ["GCCACGG", "ACCACAA",  "AGGCCTCA"],
"eye_color": ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"],
"gender": ["TGAAGGACCTTC", "TGCAGGAACTTC"],
"race":  ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]}


characters = {"eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],
"larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
"mantej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
"miha" : ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

with open("dna.txt" , "r") as dna_file:
    dna = dna_file.read()

for char in characters:
    comprobador = True
    for cha in characters[char]:
        if cha not in dna:
            comprobador = False
            break
    if comprobador  == True:
        print(char," is the thief")
