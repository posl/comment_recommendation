def bottom_count(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    return count
s = input()
print(bottom_count(s))

if __name__ == '__main__':
    bottom_count()