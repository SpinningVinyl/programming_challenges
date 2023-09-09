def char_value(char) -> int:
    freq = {'a': 3, 'b': -1, 'c': 1, 'd': 1, 'e': 4, 'f': 0, 'g': 0, 'h': 2, 'i': 2, 
            'j': -5, 'k': -2, 'l': 1, 'm': 0, 'n': 2, 'o': 3, 'p': 0, 'q': -6, 'r': 2,
            's': 2, 't': 3, 'u': 1, 'v': -1, 'w': 0, 'x': -5, 'y': 0, 'z': -7}
    return freq.get(char)

def str_value(string) -> float:
    string = string.lower()
    value = 0
    letters = 0
    for i in range(len(string)):
        if ord(string[i]) in range(97,123):
            value += char_value(string[i])
            letters += 1
    return value / letters

def shift(char, offset) -> chr:
    if ord(char) in range(97,123):
        return chr(97 + (ord(char) - 97 + offset) % 26)
    if ord(char) in range(65,91):
        return chr(65 + (ord(char) - 65 + offset) % 26)
    return char
    
def caesar(message, offset) -> str:
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_message += shift(message[i], offset)
    return encrypted_message

def reverse_caesar(message) -> str:
    decrypted_message = ""
    max_score = 0
    for i in range(27):
        test_message = caesar(message, i)
        score = str_value(test_message)
        if score > max_score:
            decrypted_message = test_message
            max_score = score
    return decrypted_message

print(caesar("fusion", 6)) # 'layout'
print(caesar("irk", 13)) # 'vex'
print(caesar("Daily Programmer!", 6)) # 'Jgore Vxumxgsskx!'
# 'Come no further, for death awaits you all with nasty, big, pointy teeth.'
print(reverse_caesar("Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky."))