# 홀짝 구분하기: 나머지연산, 조건문

def is_even(n):
    return n%2==0

def main():
    n = int(input("숫자를 입력하시오. > "))

    if is_even(n):
        print(f"{n}은 짝수입니다.")
    else:
        print(f"{n}은 홀수입니다.")


if __name__ == '__main__':
    main()