def main():
    n = int(input())
    file_list = []
    for i in range(n):
        file_list.append(input())
    for i in range(n):
        count = 0
        for j in range(i):
            if file_list[i] == file_list[j]:
                count += 1
        if count == 0:
            print(file_list[i])
        else:
            print(file_list[i] + '(' + str(count) + ')')

if __name__ == '__main__':
    main()