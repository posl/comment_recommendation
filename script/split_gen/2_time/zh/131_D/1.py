def main():
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += arr[i][0]
        if time > arr[i][1]:
            print("No")
            return
    print("Yes")
