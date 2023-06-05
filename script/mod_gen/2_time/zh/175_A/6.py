def main():
    N = int(input())
    c = input()
    #print(c)
    w = c.count('W')
    #print(w)
    r = c.count('R')
    #print(r)
    if w == 0 or r == 0:
        print(0)
        return
    i = 0
    j = N - 1
    cnt = 0
    while i < j:
        if c[i] == 'W' and c[j] == 'R':
            cnt += 1
            i += 1
            j -= 1
        elif c[i] == 'R' and c[j] == 'W':
            i += 1
            j -= 1
        elif c[i] == 'W':
            j -= 1
        elif c[j] == 'R':
            i += 1
        else:
            i += 1
            j -= 1
    print(cnt)
    return

if __name__ == '__main__':
    main()