def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(b) - max(a) + 1 if min(b) >= max(a) else 0)
