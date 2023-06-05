def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    if p == sorted(p):
        print("YES")
        return
    for i in range(N):
        for j in range(i+1, N):
            p[i], p[j] = p[j], p[i]
            if p == sorted(p):
                print("YES")
                return
            p[i], p[j] = p[j], p[i]
    print("NO")

if __name__ == '__main__':
    main()