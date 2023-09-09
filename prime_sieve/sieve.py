from math import sqrt
import sys

def count_primes(n: int) -> int:
    bool_set = [True for x in range(n + 1)]
    bool_set[0] = bool_set[1] = False
    for i in range(2, int(sqrt(n)) + 1):
        if bool_set[i]:
            j = i*i
            while j <= n:
                bool_set[j] = False
                j += i
    return len(list(filter(lambda b: b, bool_set)))

def main():
    n = 0
    if len(sys.argv) < 2 or not sys.argv[1].isdecimal():
        print('Upper limit not specified, calculating the number of primes up to 100,000')
        n = 100000
    elif sys.argv[1].isdecimal:
        n = int(sys.argv[1])
        print('Calculating the number of primes up to', f"{n:,}")
    print(count_primes(n))

if __name__ == "__main__":
    main()