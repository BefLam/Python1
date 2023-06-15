def count_occurrences(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
occurrences = count_occurrences(arr, x)
print(occurrences)
