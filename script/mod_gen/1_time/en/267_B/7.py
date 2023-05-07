def isSplit(s):
    if s[0] == '1':
        return 'No'
    else:
        for i in range(2, 11):
            if s[i-1] == '1' and s[i-2] == '1':
                return 'Yes'
        return 'No'
s = input()
print(isSplit(s))

if __name__ == '__main__':
    isSplit()