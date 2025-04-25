from math import sqrt

# 숫자 나누어서 계산하기
def divide(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return print(ans)

def main1():
    x = int(input())
    divide(x)

# 숫자를 문자로 바꿔서 계산하기
def return_to_text(x):
    sn = str(x)
    ans = 0
    for s in sn:
        ans += int(s)
    return print(ans)

def main2():
    x = int(input())
    return_to_text(x)

if __name__ == "__main__":
    main2()

