def check_shiritori(words):
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] == words[j]:
                return False
    return True

if __name__ == '__main__':
    check_shiritori()