# 세 막대(백준 : 14215 풀이)
def three_bars(i, j, k):
    arr = list({i, j, k})
    arr.sort()
    a, b, c = arr

    if a + b <= c:
        c = a + b - 1

    print(a+b+c)

def main():
    i, j, k = map(int, input().split())

    three_bars(i, j, k)

if __name__ == "__main__":
    main()

