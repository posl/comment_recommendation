def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # aをソートしておく
    a.sort()
    # bをソートしておく
    b.sort()
    # aの最小値とbの最小値を比較
    if a[0] < b[0]:
        print('Yes')
    else:
        print('No')
