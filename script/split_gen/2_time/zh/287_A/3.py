def main():
    n, x = map(int, input().split())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += a * b
    if sum <= x:
        print("Yes")
    else:
        print("No")
