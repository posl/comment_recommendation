def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum = 0
    for i in range(0, n):
        sum += a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")
