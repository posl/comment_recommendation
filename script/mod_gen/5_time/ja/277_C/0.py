def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x:x[1])
    #print(AB)
    ans = 0
    for ab in AB:
        if ab[0] >= ans:
            ans = ab[1]
    print(ans)

if __name__ == '__main__':
    main()