def check_shiritori(words):
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
        if words.count(words[i]) > 1:
            return False
    return True

if __name__ == '__main__':
    check_shiritori()