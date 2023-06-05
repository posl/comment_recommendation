def main():
    h, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if sum(a) >= h:
        print('Yes')
    else:
        print('No')
