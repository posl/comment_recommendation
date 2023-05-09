def main():
    s = input()
    #print(s)
    #print(len(s))
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += i
    print(count)
