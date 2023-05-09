def check():
    N = int(input())
    users = [input().split() for _ in range(N)]
    #print(users)
    for i in range(N):
        if users[i][0] == users[i][1]:
            return False
        for j in range(i+1,N):
            if users[i][0] == users[j][1]:
                return False
    return True

if __name__ == '__main__':
    check()