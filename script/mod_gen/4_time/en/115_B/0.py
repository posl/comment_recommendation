def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    sum = 0
    for i in range(N-1):
        sum += p[i]
    sum += p[N-1]/2
    print(int(sum))

if __name__ == '__main__':
    main()