def main():
    n,k = map(int,input().split())
    ab = []
    for i in range(n):
        a,b = map(int,input().split())
        ab.append([a,b])
    ab.sort(key=lambda x:x[0])
    now = 0
    for i in range(n):
        if ab[i][0] > now + k:
            break
        k += ab[i][1]
        now = ab[i][0]
    print(now+k)

if __name__ == '__main__':
    main()