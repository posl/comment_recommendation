def main():
    n, w = map(int, input().split())
    #print(n,w)
    req = [0] * 200005
    for i in range(n):
        s, t, p = map(int, input().split())
        req[s] += p
        req[t] -= p
    #print(req)
    for i in range(1, 200005):
        req[i] += req[i-1]
        if req[i] > w:
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()