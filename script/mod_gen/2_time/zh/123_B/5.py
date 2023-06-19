def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    #print(a,b,c,d,e)
    t = [a,b,c,d,e]
    #print(t)
    t.sort()
    #print(t)
    for i in range(5):
        if t[i]%10 == 0:
            continue
        else:
            t[i] = (t[i]//10 + 1)*10
    #print(t)
    print(sum(t))

if __name__ == '__main__':
    main()