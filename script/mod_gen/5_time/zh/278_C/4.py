def main():
    N, Q = map(int, input().split())
    follow = []
    for _ in range(Q):
        follow.append(list(map(int, input().split())))
    print(follow)
    for i in range(Q):
        if follow[i][0] == 3:
            if follow[i][1] == follow[i][2]:
                print("Yes")
            else:
                print("No")
        else:
            pass

if __name__ == '__main__':
    main()