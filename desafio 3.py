palavra = str(input("digite a palavra\n"))
tamanho = int(len(palavra))
substrings=[]
anagramas=0
#percorrendo a string e criando substrings como na questão

for b in range (1, tamanho):
    for a in range (0, tamanho):
        if a+b <= tamanho:
           substr= palavra[a:a+b]
           substrings.append(substr)
#criando uma lista que armazena listas com os valores da primeira lista
sublistas = []
alcance = len(substrings)

for n in range (0,alcance):
    sublistas.append(list(substrings[n]))
#colocando os valores em ordem alfabética, já que anagramas quando colocados em ordem alfabetica formam a mesma palavra
for list in sublistas:
    list.sort()
#contando as repetições e divindo por 2 pois percorre 2 elementos iguais
for list in sublistas:
    if sublistas.count(list) == 2:
        anagramas+=1
print (sublistas)
print (int(anagramas/2))
