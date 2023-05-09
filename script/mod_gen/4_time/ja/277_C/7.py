def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort()
    ans = 0
    for i in range(N):
        if ans < AB[i][1]:
            ans = AB[i][1]
    print(ans)
main()

if __name__ == '__main__':
    main()