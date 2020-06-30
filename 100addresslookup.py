from tree import *


def lookup100():
    f = open('Destination.txt', 'r')
    dl = f.read().split('\n')[:-1]
    r = open("Resultat du lookup.txt", "w+")
    count = 1
    for ln in dl:
        (nxt, inter) = (lookup(tree, ln)[3], lookup(tree, ln)[4])
        if nxt == '' and inter == '':
            r.write('Adresse '+str(count)+' :\t\t\t'+'Next hop : '+str(tree[0][3])+'\t\tInterface : '+str(tree[0][4]))
        else:
            r.write('Adresse ' + str(count) + ' :\t\t\t' + 'Next hop : ' + nxt + '\t\tInterface : ' + inter)
        count += 1
        r.write('\n')


lookup100()
