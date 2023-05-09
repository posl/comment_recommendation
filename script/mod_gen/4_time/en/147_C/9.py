def check_honest(i, honest_list, unkind_list):
    for j in unkind_list:
        if i == j:
            return False
    return True

if __name__ == '__main__':
    check_honest()