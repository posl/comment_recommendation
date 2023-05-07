def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = max(a)
    y = min(b)
    if x > y:
        print(0)
    else:
        print(y - x + 1)
