def main():
    n,a,b = map(int, input().split())
    p,q,r,s = map(int, input().split())
    for i in range(p, q+1):
        for j in range(r, s+1):
            if (max(1-a, 1-b) <= i <= min(n-a, n-b)) or (max(1-a, b-n) <= i <= min(n-a, b-1)):
                if (max(1-a, 1-b) <= j <= min(n-a, n-b)) or (max(1-a, b-n) <= j <= min(n-a, b-1)):
                    print("#", end="")
                    continue
            print(".", end="")
        print("")

if __name__ == '__main__':
    main()