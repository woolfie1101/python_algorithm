# 에라토스테네스의 체
def eratosthenes(n):
    result = 0
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    for i in range(2, n +1):
        if prime[i]:
            for j in range(i*2, n+1, i):
                prime[j] = False

    for a in range(n+1):
        if prime[a]:
            result += 1
    print(result)


# 백준 : 2960 풀이
def find_prime(n, k):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    cnt = 0
    for i in range(n+1):
        if is_prime[i]:
            for j in range(i, n+1, i):
                if is_prime[j] == False:
                    continue
                is_prime[j] = False
                cnt += 1

                if cnt == k:
                    return j


def main():
    N, K = map(int, input().split())
    print(find_prime(N, K))
    # n = int(input("숫자를 입력하세요: "))
    # eratosthenes(n)  # 소수 개수를 세는 함수 호출

if __name__ == "__main__":
    main()
