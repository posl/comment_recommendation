def main():
    n = int(input())
    p = list(map(int,input().split()))
    cnt = 0
    for i in range(n-1):
        if p[i] != i+1:
            cnt += 1
    if cnt <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()