def check(s):
    if s.count('?') == 10:
        return 10000
    else:
        count = 0
        for i in range(10):
            if s[i] == 'o':
                count += s.count(str(i))
            elif s[i] == 'x':
                count += 0
            else:
                count += 0
        return count

if __name__ == '__main__':
    check()