def main():
    n = int(input())
    sp = []
    for i in range(n):
        s, p = input().split()
        sp.append([s, int(p)])
    sp = sorted(sp, key=lambda x: x[1], reverse=True)
    sp = sorted(sp, key=lambda x: x[0])
    for i in range(n):
        print(sp[i][2])

if __name__ == '__main__':
    main()