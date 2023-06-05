def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(n):
        if arr[i][0] == 1:
            arr.append(arr[i][1])
        if arr[i][0] == 2:
            for j in range(arr[i][2]):
                if arr[i][1] in arr:
                    arr.remove(arr[i][1])
        if arr[i][0] == 3:
            if len(arr) > 0:
                print(max(arr) - min(arr))
            else:
                print("")
