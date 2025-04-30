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



