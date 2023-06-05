def main():
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    arr.sort()
    for i in range(n):
        if arr[i] != i+1:
            print("No")
            return
    print("Yes")
