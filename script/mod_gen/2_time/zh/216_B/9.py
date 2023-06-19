def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    names.sort()
    for i in range(N-1):
        if names[i] == names[i+1]:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()