def main():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        x -= a * b
    if x < 0:
        print("No")
    else:
        print("Yes")
