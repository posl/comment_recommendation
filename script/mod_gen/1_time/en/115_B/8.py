def  main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i % 2 == 1:
            ans += p[i]
        else:
            ans += p[i] / 2
    print(int(ans))

if __name__ == '__main__':
    ()