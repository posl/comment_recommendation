def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))

if __name__ == '__main__':
    main()