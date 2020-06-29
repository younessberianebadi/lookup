from random import randint


def prefix_gene(ip_class):
    if ip_class == 'A':
        pref = randint(8, 32)
        first_oct = bin(randint(1, 126))[2:]
    elif ip_class == 'B':
        pref = randint(8, 32)
        first_oct = bin(randint(128, 191))[2:]
    elif ip_class == 'C':
        pref = randint(8, 32)
        first_oct = bin(randint(192, 223))[2:]
    ipa_address = ''
    if len(first_oct) < 8:
        r = 8 - len(first_oct)
        re = '0' * r
        first_oct = re + first_oct
    ipa_address += first_oct
    for x in range(1, pref - 8):
        ipa_address += str(randint(0, 1))
    for x in range(pref, 32):
        ipa_address += '0'
    final = str(int(ipa_address[0:8], 2)) + '.' + str(int(ipa_address[8:16], 2)) + '.' + str(
        int(ipa_address[16:24], 2)) + '.' \
            + str(int(ipa_address[24:32], 2)) + '/' + str(pref)
    return final


# liste de next_hops

next_hop = []
for i in range(0, 4):
    next_hop.append(
        str(randint(1, 223)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 254)))

# ouvrir un fichier

f = open("FIB.txt", "w+")

# 500 adresses classe A

for b in range(1, 500):
    f.write(prefix_gene('A') + '\t\t\t' + next_hop[randint(0, 3)] + '\t\t\tS' + str(randint(1, 4)))
    f.write('\n')

# 300 adresses classe B

for c in range(1, 300):
    f.write(prefix_gene('B') + '\t\t\t'
            + next_hop[randint(0, 3)] + '\t\t\tS' + str(randint(1, 4)))
    f.write('\n')

# 200 adresses classe C

for d in range(1, 200):
    f.write(prefix_gene('C') + '\t\t\t'
            + next_hop[randint(0, 3)] + '\t\t\tS' + str(randint(1, 4)))
    f.write('\n')

# La route par defaut

f.write('0.0.0.0/0\t\t\t' + next_hop[randint(0, 3)] + '\t\t\tS' + str(randint(1, 4)))

j = open("Destination.txt", "w+")

for n in range(100):
    j.write(str(randint(1, 223)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 254))
            + '\r')
