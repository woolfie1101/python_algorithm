from math import sqrt

# 터렛(백준 : 1002 풀이)
def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) # 두 점의 거리
    diff = abs(r1 - r2) # 반지름의 차이

    ans = 0
    # 두 원이 일치 (적의 위치 무한대)
    if dist == 0 and r1 == r2:
        ans = -1
    # 적이 하나 (외접하거나 내접)
    elif r1+r2 == dist or dist == diff:
        ans = 1
    elif diff < dist < r1+r2:
        ans = 2
    else:
        ans = 0
    print(ans)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()

