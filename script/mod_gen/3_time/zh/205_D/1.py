def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    k = [int(input()) for _ in range(q)]
    for i in k:
        j = 0
        while i > 0:
            j += 1
            if j not in a:
                i -= 1
        print(j)

if __name__ == '__main__':
    main()