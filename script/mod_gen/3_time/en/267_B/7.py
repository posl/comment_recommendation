def isSplit(list1):
    if list1[0] == 0:
        return False
    else:
        columns = []
        for i in range(1, len(list1)):
            if list1[i] == 1:
                columns.append(i)
        for i in range(1, len(columns)):
            if columns[i] - columns[i - 1] > 2:
                return True
        return False
s = input()
list1 = []
for i in s:
    list1.append(int(i))

if __name__ == '__main__':
    isSplit()