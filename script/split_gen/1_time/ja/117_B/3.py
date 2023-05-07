def main():
    n = int(input())
    l = list(map(int,input().split()))
    max_l = max(l)
    l.remove(max_l)
    if sum(l) > max_l:
        print('Yes')
    else:
        print('No')
