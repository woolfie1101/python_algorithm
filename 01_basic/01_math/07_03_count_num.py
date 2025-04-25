from math import sqrt

# 숫자의 개수(백준 : 2577 풀이)
def solve(n):
    sn = str(n)
    ans = [0] * 10
    for s in sn:
        ans[int(s)] += 1
    for i in ans:
        print(i)

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    solve(A * B * C)

if __name__ == "__main__":
    main()