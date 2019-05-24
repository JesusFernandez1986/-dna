characters = {"eva": ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"],  #cambiamos las caracteristicas por su valor en la cadena de adn
"larisa": ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"],
"mantej": ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"],
"miha" : ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]}

with open("dna.txt" , "r") as dna_file: # abrimos el archivo en modo escritura y guardamos su valor dentro de la variable dna
    dna = dna_file.read()

for char in characters:             #este bucle recorre los elementos de el diccionario caracters y dentro de cada elemento recorre cada subelemento
    comprobador = True
    for cha in characters[char]:
        if cha not in dna:          #si algun elemento de la lista dentro del diccionario no esta en dna cambimos a false la variable y salimos del bucle al siguiente elemento
            comprobador = False
            break
    if comprobador  == True:        #si todos los elementos de la lista estan dentro de la variable dn, la variable comprobador nunca sera false, y por lo tanto, ese sera el culpable
        print(char," is the thief")
