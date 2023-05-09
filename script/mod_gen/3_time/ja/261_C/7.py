def main():
    n = int(input())
    file_dict = {}
    for i in range(n):
        file_name = input()
        if file_name in file_dict:
            file_dict[file_name] += 1
            print(file_name + "(" + str(file_dict[file_name]) + ")")
        else:
            file_dict[file_name] = 0
            print(file_name)

if __name__ == '__main__':
    main()