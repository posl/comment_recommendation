def main():
    s = [input() for i in range(10)]
    #print(s)
    for i in range(10):
        if s[i].find('#') != -1:
            start = i
            break
    for i in range(9, -1, -1):
        if s[i].find('#') != -1:
            end = i
            break
    for i in range(10):
        if s[i].find('#') != -1:
            start2 = s[i].find('#')
            break
    for i in range(9, -1, -1):
        if s[i].find('#') != -1:
            end2 = s[i].rfind('#')
            break
    print(start+1, end+1)
    print(start2+1, end2+1)

if __name__ == '__main__':
    main()