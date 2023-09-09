def nonogramrow(binary_list):
    binary_string = ''.join([str(x) for x in binary_list])
    int_list = []
    fragments = binary_string.split('0')
    for fragment in fragments:
        if len(fragment) > 0:
            int_list.append(len(fragment))
    return int_list

# same thing but completely unreadable
def nonogramrow2(binary_list):
    return list(map(lambda s: len(s), list(filter(lambda s: len(s) > 0, ''.join([str(x) for x in binary_list]).split('0')))))

print(nonogramrow2([0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]))
