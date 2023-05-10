def main():
    n, w = map(int, input().split())
    a = [0]*(2*10**5+1)
    for i in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(2*10**5):
        a[i+1] += a[i]
        if a[i] > w:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()