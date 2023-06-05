def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    t = [a,b,c,d,e]
    m = 0
    for i in range(5):
        if m < t[i]%10:
            m = t[i]%10
            n = i
    for i in range(5):
        if i != n:
            t[i] = t[i] + 10 - t[i]%10
    print(sum(t))

if __name__ == '__main__':
    main()