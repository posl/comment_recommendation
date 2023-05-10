def check(s):
    if len(set(s)) == 2:
        for i in set(s):
            if s.count(i) != 2:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    check()