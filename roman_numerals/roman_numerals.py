def roman_to_decimal(roman_numeral: str) -> int:
    roman_numeral = roman_numeral.upper()
    result = 0
    pos = 0
    val = 0
    while (pos < len(roman_numeral)):
        if roman_numeral[pos] == 'M':
            val = 1000
        elif roman_numeral[pos] == 'D':
            val = 500
        elif roman_numeral[pos] == 'C':
            val = 100
        elif roman_numeral[pos] == 'L':
            val = 50
        elif roman_numeral[pos] == 'X':
            val = 10
        elif roman_numeral[pos] == 'V':
            val = 5
        elif roman_numeral[pos] == 'I':
            if pos == len(roman_numeral) - 1 or roman_numeral[pos + 1] == 'I':
                val = 1
            elif roman_numeral[pos + 1] == 'X':
                val = 9
                pos += 1
            elif roman_numeral[pos + 1] == 'V':
                val = 4
                pos += 1
        result += val
        pos += 1
    return result

def numcompare(a: str, b: str) -> bool:
    return roman_to_decimal(a) < roman_to_decimal(b)

def main():
    print(numcompare("I", "I"))
    print(numcompare("I", "II"))
    print(numcompare("II", "I"))
    print(numcompare("V", "IIII"))
    print(numcompare("MDCLXV", "MDCLXVI"))
    print(numcompare("MM", "MDCCCCLXXXXVIIII"))

if __name__ == "__main__":
    main()
