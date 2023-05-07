def main():
    N = int(input())
    user = []
    for i in range(N):
        user.append(input().split())
    #print(user)
    for i in range(N):
        #print("i:",i)
        for j in range(N):
            #print("j:",j)
            if i == j:
                continue
            if user[i][0] == user[j][1]:
                print("No")
                return
    print("Yes")
    return
main()

if __name__ == '__main__':
    main()