def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    result = 0
    for i in range(n):
        result += a[i] * b[i]
    if result == 0:
        print("Yes")
    else:
        print("No")
