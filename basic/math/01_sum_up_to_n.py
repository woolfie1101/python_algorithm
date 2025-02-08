# 1. for 문으로 합계 구하기
def sum_with_for(n):
    result = 0
    for i in range(1, n+1):
        result += i
    print(result)

# 2. while 문 사용하기
def sum_sith_while(n):
    cnt = 1
    result = 0
    while cnt <= n:
        result += cnt
        cnt += 1
    print(result)

# 3. 내장 함수 사용
def inner_function(n):
    print(sum(range(1, n+1)))

# 4. 수열의 합 구하는 공식으로 구하기
def sequence_sum(n):
    result = (1+n) * n /2
    print(result)

# 5. 합(백준) : https://www.acmicpc.net/problem/8393
def problem_8393(n):
    print((1+n) * n /2)


# main 함수로 호출

def main():
    n = int(input('n값을 입력해주세요: '))
    problem_8393(n)

if __name__ == "__main__":
    main()