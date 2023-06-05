def main():
    N = int(input())
    w = list(map(int, input().split()))
    w.sort()
    t = sum(w)
    s = 0
    for i in range(N-1):
        s += w[i]
        if s*2 >= t:
            print(min(s*2-t, t-s*2+w[i+1]))
            break

if __name__ == '__main__':
    main()