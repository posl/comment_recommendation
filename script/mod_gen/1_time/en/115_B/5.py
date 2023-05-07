def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    for i in range(N-1):
        p[i] /= 2
    print(int(sum(p)))

if __name__ == '__main__':
    main()