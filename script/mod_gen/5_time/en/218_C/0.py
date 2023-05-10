def is_same(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i][j] != list2[i][j]:
                return False
    return True

if __name__ == '__main__':
    is_same()