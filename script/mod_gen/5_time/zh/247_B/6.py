def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()