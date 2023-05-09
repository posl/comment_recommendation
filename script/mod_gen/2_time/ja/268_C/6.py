def main():
    N = int(input())
    p = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            if i != 0 and i != N-1:
                p[i],p[i+1] = p[i+1],p[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()