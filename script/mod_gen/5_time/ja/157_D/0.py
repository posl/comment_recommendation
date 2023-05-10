def main():
    n, m, k = map(int, input().split())
    ab = []
    cd = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    for i in range(k):
        cd.append(list(map(int, input().split())))
    #print(n, m, k)
    #print(ab)
    #print(cd)
    #print()

if __name__ == '__main__':
    main()