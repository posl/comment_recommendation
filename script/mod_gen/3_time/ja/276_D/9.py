def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    while True:
        if all(a%2==0 for a in A):
            A = [a//2 for a in A]
            cnt += 1
        else:
            break
    if all(a==A[0] for a in A):
        print(cnt)
    else:
        print(-1)

if __name__ == '__main__':
    main()