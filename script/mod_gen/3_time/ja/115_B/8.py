def main():
    N = int(input())
    p = list()
    for i in range(N):
        p.append(int(input()))
    p.sort()
    print(sum(p) - int(p[-1]/2))

if __name__ == '__main__':
    main()