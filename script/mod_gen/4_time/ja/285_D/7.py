def main():
    n = int(input())
    users = []
    for _ in range(n):
        users.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if users[i][0] == users[j][0] or users[i][1] == users[j][1]:
                    print('No')
                    return
    print('Yes')
main()
