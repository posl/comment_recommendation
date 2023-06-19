def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if sorted(a) == list(range(1, n+1)):
        print('Yes')
    else:
        print('No')
