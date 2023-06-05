def isTwoCharacter(s):
    if len(s) != 4:
        return False
    if len(set(s)) == 2:
        for c in set(s):
            if s.count(c) != 2:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    isTwoCharacter()