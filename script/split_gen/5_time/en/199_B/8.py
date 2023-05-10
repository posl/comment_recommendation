def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max = min(b) - max(a) + 1
    if max > 0:
        print(max)
    else:
        print(0)
