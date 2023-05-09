def main():
    N = int(input())
    names = []
    for i in range(N):
        name = input().split()
        names.append(name)
    for i in range(N-1):
        for j in range(i+1,N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()