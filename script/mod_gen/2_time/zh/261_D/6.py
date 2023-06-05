def main():
    n = int(input())
    file = []
    for i in range(n):
        file.append(input())
    file_set = set(file)
    file_dict = {}
    for i in file_set:
        file_dict[i] = 0
    for i in range(n):
        if file[i] in file_set:
            file_set.remove(file[i])
            file_dict[file[i]] += 1
        if file_dict[file[i]] == 0:
            print(file[i])
        else:
            print(file[i] + "(" + str(file_dict[file[i]]) + ")")

if __name__ == '__main__':
    main()