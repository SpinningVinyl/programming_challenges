def next_palindrome(value):
    value = str(value + 1)
    length = len(value)
    if length % 2 == 0:
        left_half = value[:length // 2]
        right_half = value[length // 2:]
        if left_half[::-1] == right_half:
            return int(value)
        if int(left_half[::-1]) > int(right_half):
            return int(left_half + left_half[::-1])
        if int(left_half[::-1]) < int(right_half):
            left_half = str(int(left_half) + 1)
            return int(left_half + left_half[::-1])
    else:
        left_half = value[:length // 2]
        right_half = value[length // 2 + 1:]
        middle = value[length // 2]
        if left_half[::-1] == right_half:
            return int(value)
        if int(left_half[::-1]) > int(right_half):
            return int(left_half + middle + left_half[::-1])
        if int(left_half[::-1]) < int(right_half):
            if int(middle) < 9:
                middle = str(int(middle) + 1)
                return int(left_half + middle + left_half[::-1])
            else:
                left_half = str(int(left_half) + 1)
                right_half = left_half[::-1]
                middle = '0' if len(left_half + right_half) < length else ''
                return int(left_half + middle + right_half)

print(next_palindrome(808))
print(next_palindrome(999))
print(next_palindrome(2133))
print(next_palindrome(3**39))
print(next_palindrome(1998))
print(next_palindrome(192))
print(next_palindrome(2114))
print(next_palindrome(21023))