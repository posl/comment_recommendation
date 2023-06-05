def check_list(list):
    for i in range(0,len(list)):
        if list[i] == 0:
            return False
    return True

if __name__ == '__main__':
    check_list()