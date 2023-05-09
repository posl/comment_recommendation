def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if name[i][0] == name[j][0] and i != j:
                print("No")
                return
            if name[i][1] == name[j][1] and i != j:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()