def main():
    N = int(input())
    p = list(map(int, input().split()))
    p2 = sorted(p)
    if p == p2:
        print("YES")
    else:
        count = 0
        for i in range(N):
            if p[i] == p2[i]:
                pass
            else:
                count += 1
        if count == 2:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()