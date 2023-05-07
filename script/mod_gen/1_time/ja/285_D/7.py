def main():
    N = int(input())
    users = []
    for i in range(N):
        users.append(input().split())
    #print(users)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if users[i][0] == users[j][1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()