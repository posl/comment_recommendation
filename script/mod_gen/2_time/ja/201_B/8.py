def main():
    n = int(input())
    m = {}
    for i in range(n):
        s, t = input().split()
        m[s] = int(t)
    #print(m)
    m = sorted(m.items(), key=lambda x:x[1], reverse=True)
    print(m[1][0])

if __name__ == '__main__':
    main()