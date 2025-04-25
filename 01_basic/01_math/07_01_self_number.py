from math import sqrt

# 셀프 넘버(백준 : 4673 풀이)
def d(n):
    my_sum = n
    while n:
        my_sum += n % 10
        n //= 10
    return my_sum

def main():
    MAX = 10_000 + 1
    my_arr = [True] * MAX
    for i in range(1, MAX):
        rst = d(i)
        if rst < MAX:
            my_arr[rst] = False

    for i in range(1, MAX):
        if my_arr[i]:
            print(i)

if __name__ == "__main__":
    main()