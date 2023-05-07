def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n):
        for j in range(n):
            if i != j and names[i] == names[j]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()