def main():
    N = int(input())
    p = list(map(int,input().split()))
    p2 = sorted(p)
    count = 0
    for i in range(N):
        if p[i] != p2[i]:
            count += 1
    if count <= 2:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()