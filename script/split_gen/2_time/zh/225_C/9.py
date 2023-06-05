def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if a[0] == 1:
        for i in range(1, n):
            if a[i] != i+1:
                print('No')
                break
        else:
            print('Yes')
    else:
        print('No')
