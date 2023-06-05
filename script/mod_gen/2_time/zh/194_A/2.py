def main():
    k = int(input())
    s = input()
    t = input()
    s = s[:4]
    t = t[:4]
    s = [int(i) for i in s]
    t = [int(i) for i in t]
    s.sort()
    t.sort()
    s.reverse()
    t.reverse()
    s = [i for i in s if i != 9]
    t = [i for i in t if i != 9]
    s = ['9' if i == 6 else str(i) for i in s]
    t = ['9' if i == 6 else str(i) for i in t]
    s = int(''.join(s))
    t = int(''.join(t))
    s = s * 1000
    t = t * 1000
    s = s + 999
    t = t + 999
    s = s - (k * 1000)
    t = t - (k * 1000)
    if s > t:
        print(1)
        return
    elif s == t:
        print(0.5)
        return
    else:
        print(0)
        return

if __name__ == '__main__':
    main()