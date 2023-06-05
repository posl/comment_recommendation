def main():
    n = int(input())
    filenames = []
    for i in range(n):
        filenames.append(input())
    filenames_set = set()
    for i in range(n):
        if filenames[i] not in filenames_set:
            print(filenames[i])
            filenames_set.add(filenames[i])
        else:
            num = 1
            while True:
                if filenames[i] + '(' + str(num) + ')' not in filenames_set:
                    print(filenames[i] + '(' + str(num) + ')')
                    filenames_set.add(filenames[i] + '(' + str(num) + ')')
                    break
                else:
                    num += 1

if __name__ == '__main__':
    main()