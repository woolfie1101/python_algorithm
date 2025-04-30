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


arr = [3,1,4,5,2]
# 삽입 정렬1
def insertion_sort(arr):
    new_arr = [arr[0]]
    print(f"1 번째 정렬된 리스트 = {new_arr}")
    for i in range(1, len(arr)):
        j = 0
        while j < i and new_arr[j] < arr[i]:
            j += 1
        new_arr.insert(j, arr[i])
        print(f"{i + 1} 번째 정렬된 리스트 = {new_arr}")
    return new_arr
print("최종 정렬된 리스트 =", insertion_sort(arr))


arr = [3,1,4,5,2]
# 삽입 정렬2
def insertion_sort2(arr):
    for i in range(1, len(arr)):
        print(f"{i} 번째 새로운 리스트 = {arr[:i]} 기존 리스트 = {arr[i:]}")
        j = i
        while 0 < j and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
print("정렬이 끝난 리스트 =", insertion_sort2(arr))