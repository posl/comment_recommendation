def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()