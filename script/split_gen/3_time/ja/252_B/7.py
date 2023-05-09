def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    b_i = 0
    for i in range(n):
        if i == b[b_i]-1:
            b_i += 1
            continue
        else:
            print('Yes')
            exit()
    print('No')
