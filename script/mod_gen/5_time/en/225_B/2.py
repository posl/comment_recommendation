def main():
    N = int(input())
    a = [0]*(N-1)
    b = [0]*(N-1)
    for i in range(N-1):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b.count(1) == N-1:
        print('Yes')
    else:
        print('No')
main()
