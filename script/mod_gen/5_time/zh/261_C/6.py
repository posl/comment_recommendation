def main():
    n = int(input())
    file = []
    for i in range(n):
        file.append(input())
    for i in range(n):
        if file[i] not in file[:i]:
            print(file[i])
        else:
            for j in range(i):
                if file[j] == file[i]:
                    k = file[:i].count(file[i])
                    print(file[i] + "(" + str(k) + ")")
                    break

if __name__ == '__main__':
    main()