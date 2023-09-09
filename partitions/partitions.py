offset_cache = {}

def offset(n: int) -> int:
    if n < 0: return 0
    m = 0
    if n in offset_cache: return offset_cache[n]
    if n % 2 == 0:
        m = - n // 2
    else:
        m = n // 2 + 1
    result = (3 * m * m - m) // 2
    offset_cache[n] = result
    return result

p_cache = {}

def p(n: int) -> int:
    if n < 0: return 0
    if n <= 1: return 1
    if n in p_cache: return p_cache[n]
    o = offset(1)
    i = 0
    result = 0
    while o <= n:
        result += p(n - o) * (((i // 2) % 2) * -2 + 1)
        i += 1
        o = offset(i + 1)
    p_cache[n] = result 
    return result

print('p(666)', p(666))