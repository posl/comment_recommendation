def main():
    N = int(input())
    mnt = []
    for i in range(N):
        s, t = input().split()
        mnt.append([s, int(t)])
    mnt.sort(key=lambda x: x[1], reverse=True)
    print(mnt[1][0])

if __name__ == '__main__':
    main()