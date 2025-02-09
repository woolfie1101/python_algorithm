# 소수 구하기1
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 소수 개수 구하기
def cnt_prime(n):
    cnt = 0
    for i in range(2, n+1):
        if is_prime(i):
            cnt += 1
    print(cnt)

# 소수 구하기2
def is_prime_2(n):
    result = 0
    list_num = []  # 소수를 저장할 리스트
    for i in range(2, n):
        if solve_prime(i):
            list_num.append(i)  # 소수를 리스트에 추가
            result += 1
    print("소수 개수:", result)
    print("소수 목록:", list_num)

def solve_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("숫자를 입력하세요: "))
    is_prime_2(n)  # 소수 개수를 세는 함수 호출

if __name__ == "__main__":
    main()