def  main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    for _ in range(4):
        s = rotate(s, n)
        if s == t:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    ()