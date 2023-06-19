def func(s):
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'a':
            return i+1
    return -1

if __name__ == '__main__':
    func()