def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    for i in range(n):
        for j in range(i+1, n):
            if name[i] == name[j]:
                print('Yes')
                exit(0)
    print('No')

if __name__ == '__main__':
    main()