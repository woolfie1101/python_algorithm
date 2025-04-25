from math import sqrt

# 벌집(백준 : 2292 풀이)
def solve(x):
    a = 1
    n = 1
    while a < x:
        a += 6 * n
        n += 1
    print(n)

def main():
    x = int(input())
    solve(x)

if __name__ == "__main__":
    main()

