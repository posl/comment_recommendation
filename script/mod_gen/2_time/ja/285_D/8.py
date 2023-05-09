def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if names[i][1] == names[j][0]:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()