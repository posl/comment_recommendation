def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    print(sum(p[0:-1]) + p[-1] // 2)

if __name__ == '__main__':
    main()