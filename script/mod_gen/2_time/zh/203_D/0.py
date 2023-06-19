def median(lst):
    lst.sort()
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) // 2

if __name__ == '__main__':
    median()