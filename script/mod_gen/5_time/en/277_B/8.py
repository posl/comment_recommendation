def check_unique(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False

if __name__ == '__main__':
    check_unique()