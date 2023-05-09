def main():
    N = int(input())
    mtn = []
    for i in range(N):
        mtn.append(input().split())
    mtn.sort(key=lambda x: int(x[1]), reverse=True)
    print(mtn[1][0])

if __name__ == '__main__':
    main()