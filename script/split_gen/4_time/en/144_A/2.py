def main():
    a, b = map(int, input().split())
    if (1 <= a and a <= 20) and (1 <= b and b <= 20):
        print(a*b)
    else:
        print(-1)
