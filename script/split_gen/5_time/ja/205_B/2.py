def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    if a == b:
        print('Yes')
    else:
        print('No')
