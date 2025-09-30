def binary_search(arr, target):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            start = (mid + 1)
        else:
            end = (mid - 1)
    return -1

def binary_recurrsive(arr, target, start, end):
    if end >= start:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            print(mid+1)
            return binary_search(mid+1)
        else:
            return binary_search(mid -1)

arr = [1,2,3,4,5,8,9,10,11,14,15,16,17,18,20]
print(arr)
print("---------------------------------------------------")
target = int(input("Enter the number you to find: "))
result = binary_search(arr, target)

if result != -1:
    print("Element is present in the list:", result + 1) 
else:
    print("Element is not found in the list.")
# def binary():


# print(len(arr))

