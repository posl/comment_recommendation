def last_index(str, c):
    for i in range(len(str), 0, -1):
        if str[i-1] == c:
            return i
    return -1
s = input()
print(last_index(s, 'a'))

if __name__ == '__main__':
    last_index()