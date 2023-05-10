def main():
    N = int(input())
    users = []
    for i in range(N):
        users.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j and users[i][0] == users[j][1]:
                users[i][0] = users[j][0]
                break
    for i in range(N):
        for j in range(N):
            if i != j and users[i][1] == users[j][0]:
                users[i][1] = users[j][1]
                break
    for i in range(N):
        if users[i][0] == users[i][1]:
            print("No")
            return
    print("Yes")
