def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    names.sort()
    for i in range(n-1):
        if names[i] == names[i+1]:
            print("Yes")
            break
        elif i == n-2:
            print("No")

if __name__ == '__main__':
    main()