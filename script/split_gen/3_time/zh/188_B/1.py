def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    sum = 0
    for i in range(n):
        sum = sum + a[i] * b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")
