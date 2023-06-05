def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if a[i] > n:
            print("No")
            return
        b[a[i] - 1] += 1
    for i in range(n):
        if b[i] != 1:
            print("No")
            return
    print("Yes")
