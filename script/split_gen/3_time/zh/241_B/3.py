def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a.sort()
    # b.sort()
    # a.reverse()
    # b.reverse()
    # if b[0] > a[0]:
    #     print('No')
    # else:
    #     print('Yes')
    a.sort()
    b.sort()
    a.reverse()
    b.reverse()
    for i in range(n):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')
    return
