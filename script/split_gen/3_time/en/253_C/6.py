def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    print(arr)
    for i in range(n):
        if arr[i][0] == 1:
            arr.append(arr[i][1])
        elif arr[i][0] == 2:
            if arr[i][1] in arr:
                arr.remove(arr[i][1])
        elif arr[i][0] == 3:
            print(max(arr)-min(arr))
