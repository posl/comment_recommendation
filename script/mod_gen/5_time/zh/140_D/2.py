def happyPeople(s):
    n = len(s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    return count

if __name__ == '__main__':
    happyPeople()