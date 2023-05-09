def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print('Yes' if l[-1] < sum(l[:-1]) else 'No')
