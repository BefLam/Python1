def find_closest(arr, x):
    closest_num = arr[0]
    min_diff = abs(x - arr[0])
    for num in arr:
        diff = abs(x - num)
        if diff < min_diff:
            min_diff = diff
            closest_num = num
    return closest_num
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
closest = find_closest(arr, x)
print(closest)