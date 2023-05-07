def isSplit(s):
    if s[0] == '0':
        return 'No'
    else:
        for i in range(1, 9):
            if s[i] == '1':
                if s[i-1] == '1' and s[i+1] == '1':
                    return 'Yes'
        return 'No'
s = input()
print(isSplit(s))

if __name__ == '__main__':
    isSplit()