arr = [3,1,4,5,2]

# 정렬
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

#연습
n=len(arr)
for i in range(n):
    print(i)

arr = [3,1,4,5,2]
# 선택 정렬
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'{i+1}번째 정렬 후 = {arr}')
    return arr
print(selection_sort(arr))

arr = [3,1,4,5,2]
# 거품 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f'버블 정렬 변경 리스트 = {arr}')
    return arr
print(f'버블 정렬 : {bubble_sort(arr)}')

