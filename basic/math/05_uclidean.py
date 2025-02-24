# 최대 공약수
def common_divisor(a, b):
    n = a if a < b else b
    for i in range(n, 0, -1):
        if a % i == 0 and b % i == 0:
            print(i)
            break

# 유클리드 호제법
def uclidean(a, b):
    if a < b:
        small = a
        big = b
    else:
        small = b
        big = a
    if big % small == 0:
        print(small)
    else:
        uc_result(big, small)

def uc_result(big, small):
    if big % small == 0:
        print(small)
    else:
        result = big % small
        uc_result(small, result)

def main():
    a, b = map(int, input().split())
    uclidean(a, b)

if __name__ == "__main__":
    main()

