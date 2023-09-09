coins = [500, 100, 25, 10, 5, 1]

def change(n: int) -> int:
    index = 0
    count = 0
    remainder = n
    while remainder > 0:
        count += remainder // coins[index]
        remainder %= coins[index]
        index += 1
    return count

print('change(0) =', change(0))
print('change(12) =', change(12))
print('change(468) =', change(468))
print('change(123456) =', change(123456))