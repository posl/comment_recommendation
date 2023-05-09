def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()