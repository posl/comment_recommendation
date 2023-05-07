def median(lst):
    lst.sort()
    return lst[len(lst) // 2]

if __name__ == '__main__':
    median()