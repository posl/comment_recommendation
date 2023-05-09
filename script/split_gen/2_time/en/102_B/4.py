def main():
    n = int(input())
    a = list(map(int, input().split()))
    max1 = max(a)
    min1 = min(a)
    print(max1 - min1)
