# 함수 이용하기
def use_function(n):
    num = list(n)
    print(min(num))
    print(max(num))

# 반복문 사용하기
def use_for(n):
    max_val = 0
    min_val = next(n)
    for a in n:
        if max_val < a:
            max_val = a
        if min_val > a:
            min_val = a
    print(min_val)
    print(max)

# 숫자 범위 고려하기
def arrange_num(n):
    num = list(n)
    max_val = num[0]
    for a in num[1:]:
        if max_val < a:
            max_val = a
    print(max_val)

# 백준 : 10818 첫번째 풀이
def num_10818_1st(n):
    m = list(n)
    min_val = m[0]
    max_val = m[0]
    for a in m:
        if max_val < a:
            max_val = a
        if min_val > a:
            min_val = a
    print(min_val, max_val)

# 백준 : 10818 두번째 풀이
def num_10818_2nd(n):
    m = list(n)
    print(min(m), max(m))


def main():
    n = map(int, input().split())
    num_10818_2nd(n)

if __name__ == "__main__":
    main()