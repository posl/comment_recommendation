def check_shiritori(words):
    for i in range(1, len(words)):
        if words[i] in words[:i]:
            return False
        if words[i][0] != words[i-1][-1]:
            return False
    return True

if __name__ == '__main__':
    check_shiritori()