def lookup(tr, add_lookup):
    tab = add_lookup.split(".")
    binary_conversion = {}
    for x in range(0, 4):
        binary_conversion[x] = bin(int(tab[x]))[2:]
    look = ''
    for x in range(0, 4):
        if len(binary_conversion[x]) < 8:
            r = 8 - len(binary_conversion[x])
            re = '0' * r
            binary_conversion[x] = re + binary_conversion[x]
        look += binary_conversion[x]
    current_node = tr[0]
    if look == '00000000000000000000000000000000':
        return tr[0]
    else:
        for i in range(0, len(look)):
            if look[i] == '0':
                if current_node[1] != '':
                    for s in range(0, len(tr)):
                        if tr[s][0] == current_node[1]:
                            current_node = tr[s]
            else:
                if current_node[2] != '':
                    for s in range(0, len(tr)):
                        if tr[s][0] == current_node[2]:
                            current_node = tr[s]
        return current_node


def create():
    f = open('FIB.txt', 'r')
    tree = [['root', '', '', '', '']]
    c = 0
    fib_lines = f.read().split('\n')
    for i in range(0, len(fib_lines)):
        pref_gotten = fib_lines[i].split('\t\t\t')[0]
        mask = pref_gotten.split('/')[1]
        address_prefix = pref_gotten.split('/')[0]
        tab = address_prefix.split(".")
        bintab = {}
        for x in range(0, 4):
            bintab[x] = bin(int(tab[x]))[2:]
        expanded_address = ''
        for x in range(0, 4):
            if len(bintab[x]) < 8:
                r = 8 - len(bintab[x])
                re = '0' * r
                bintab[x] = re + bintab[x]
            expanded_address += bintab[x]
        net_id = expanded_address[0:int(mask)]
        current_node = tree[0]
        for n in range(0, len(net_id)):
            if net_id[n] == '0':
                if current_node[1] == '':
                    tree.append(['node-' + str(c), '', '', '', ''])
                    current_node[1] = 'node-' + str(c)
                    c += 1
                    current_node = tree[len(tree) - 1]
                else:
                    for s in range(0, len(tree)):
                        if tree[s][0] == current_node[1]:
                            current_node = tree[s]
            elif net_id[n] == '1':
                if current_node[2] == '':
                    tree.append(['node-' + str(c), '', '', '', ''])
                    current_node[2] = 'node-' + str(c)
                    c += 1
                    current_node = tree[len(tree) - 1]
                else:
                    for s in range(0, len(tree)):
                        if tree[s][0] == current_node[2]:
                            current_node = tree[s]
        current_node[3] = fib_lines[i].split('\t\t\t')[1]
        current_node[4] = fib_lines[i].split('\t\t\t')[2]
    return tree


tree = create()
# print(lookup('196.113.32.0'))
