from lec01.lec01_03_primenum import is_prime

def main():
    # primes = []
    # for i in range(2,51):
    #     if is_prime(i):
    #         primes.append(i)
    # print(primes)

    print([i for i in range(2,51) if is_prime(i)])

if __name__ == '__main__':
    main()