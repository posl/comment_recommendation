def check_shiritori(words):
    for i in range(len(words)):
        if i > 0 and words[i][0] != words[i-1][-1]:
            return False
        if words.count(words[i]) > 1:
            return False
    return True

if __name__ == '__main__':
    check_shiritori()