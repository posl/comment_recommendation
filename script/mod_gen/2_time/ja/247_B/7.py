def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    flag = True
    for i in range(N):
        for j in range(N):
            if i != j:
                if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                    flag = False
    if flag:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()