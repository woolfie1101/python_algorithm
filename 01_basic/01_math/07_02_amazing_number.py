from math import sqrt

# 신기한 수(백준 : 17618 풀이)
def weird(n):
    sn = str(n)
    ans = 0
    for i in sn:
        ans += int(i)
    if n % ans == 0:
        return True
    return False

def find(n):
    ans = 0
    for i in range(1, n+1):
        if weird(i):
            ans += 1
    return print(ans)

def main():
    x = int(input())
    find(x)

if __name__ == "__main__":
    main()