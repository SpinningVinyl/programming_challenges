def binomial(x, n, k):
    result = 0
    aux = 1
    for i in range(1, n + 1):
        aux *= (x + 1 - i) / i
        result += aux
        if (result > k):
            break
    return int(result)

def speedy_drops(phones, floors):
    lower = 0
    upper = floors
    mid = (upper + lower) // 2
    
    while upper - lower > 1:
        mid = lower + (upper - lower) // 2
        if binomial(mid, phones, floors) < floors:
            lower = mid
        else:
            upper = mid
    return lower + 1

def phones(floors, drops):
    for i in range (1, floors):
        if speedy_drops(i, floors) == drops:
            return i
    return -1
