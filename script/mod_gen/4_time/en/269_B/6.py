def main():
    #print("Hello World!")
    s = []
    for i in range(10):
        s.append(input())
    #print(s)
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if "#" in s[i]:
            a = i+1
            break
    for i in range(9, -1, -1):
        if "#" in s[i]:
            b = i+1
            break
    #print(a)
    #print(b)
    for i in range(10):
        if "#" in s[i]:
            c = s[i].index("#")+1
            break
    for i in range(9, -1, -1):
        if "#" in s[i]:
            d = s[i].index("#")+1
            break
    #print(c)
    #print(d)
    print(str(a)+" "+str(b))
    print(str(c)+" "+str(d))
    return 0

if __name__ == '__main__':
    main()