def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    print(int(sum(p) - p[-1]/2))

if __name__ == '__main__':
    main()