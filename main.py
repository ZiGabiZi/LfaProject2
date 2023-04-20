with open("ex.txt", 'r') as f:
    Lst = f.readline().split()
    Lalf = f.readline().split()
    L = []
    aux = f.readline()
    while aux:
        L.append(aux.strip().split())
        aux = f.readline()
    init = L[len(L)-2]
    fin = L[len(L)-1]
    L.remove(L[len(L)-2])
    L.remove(L[len(L)-1])
print(L)

K = []
for i in Lst:
    K.append(i)
init = init[0]

for i in range(len(K)):
    if K[i] == init:
       K[i] = 1


aux2 = []
aux = [init]

while aux != []:
    for j in range(len(aux)):
        for i in range(len(L)):
            if L[i][0] == aux[j]:
                if L[i][2] in K:
                    aux2.append(L[i][2])
    aux.clear()
    aux += aux2
    aux2.clear()

    for j in aux:
        for x in range(len(K)):
            if K[x] == j:
                K[x] = 1

for i in range(len(K)):
    if K[i] != 1:
        for j in L:
            if j[0]==K[i] or j[2] == K[i]:
                L.remove(j)
        for x in Lst:
            if x == K[i]:
                Lst.remove(x)

Lmin = [[], fin]
for j in Lst:
    if j not in fin:
        Lmin[0].append(j)

print(Lmin)




Laux3 = Lmin
ok_fin = 0

while ok_fin == 0:
    ok_fin = 0
    Lmin = Laux3
    Lechiv = []

    for liste in range(len(Lmin)):
        for element in range(len(Lmin[liste])):
            List = []
            for lista_reguli in L:
                if lista_reguli[0] == Lmin[liste][element]:
                    List.append([lista_reguli[1], lista_reguli[2]])

            for element2 in range(element+1, len(Lmin[liste])):
                List2 = []
                for lista_reguli2 in L:
                    if lista_reguli2[0] == Lmin[liste][element2]:
                        List2.append([lista_reguli2[1], lista_reguli2[2]])

                ok = 1
                for i in range(len(Lalf)):
                    for j in Lmin:
                        if (((List[i][1] not in j) and (List2[i][1] in j)) or ((List2[i][1] not in j) and (List[i][1] in j))):
                            ok = 0
                            break
                if ok == 0:
                    Lechiv.append([Lmin[liste][element], "NU", Lmin[liste][element2]])
                else:
                    Lechiv.append([Lmin[liste][element], Lmin[liste][element2]])

        if len(Lmin[liste]) == 1:
            Lechiv.append(Lmin[liste])

    for j in Lst:
        for i in Lechiv:
            oki = 0
            if j in i:
                ok = 1
                break
        if oki == 0:
            Lechiv.append([j])




    Lechiv2 = [i for i in Lechiv if len(i) != 3]

    print(Lechiv2)


    Laux2 = []
    for i in Lechiv2:
        if i not in Laux2:
            Laux2.append(i)
    print(Laux2, "OK")


# -------------------------------------------------------------------

    def Concat3(L):
        L2 = L
        ok = 0
        while ok == 0:
            Laux = []
            Laux2 = [0 for i in range(len(L2))]
            for i in range(len(L2)):
                for j in range(i+1, len(L2)):
                    if any(item in L2[i] for item in L2[j]) and list(set(L2[i]+L2[j])) not in Laux:
                        Laux.append(list(set(L2[i]+L2[j])))
                        Laux2[i] = 1
                        Laux2[j] = 1
                    elif any(item in L2[i] for item in L2[j]) and list(set(L2[i]+L2[j])) in Laux:
                        Laux2[i] = 1
                        Laux2[j] = 1

            for i in range(len(Laux2)):
                if Laux2[i] == 0:
                    Laux.append(L2[i])

            ok = 1
            for i in range(len(Laux)):
                for j in range(i+1, len(Laux)):
                    if any(item in Laux[i] for item in Laux[j]):
                        ok = 0
            L2 = Laux
        return L2






    print(Laux2)
    Laux3 = Concat3(Laux2)
    if Lmin == Laux3:
        ok_fin = 1
    print(Laux3)






