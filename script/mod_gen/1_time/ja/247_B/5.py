def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()