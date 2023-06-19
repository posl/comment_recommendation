def solve():
    s = input()
    k = int(input())
    #print(s, k)
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print(1)

if __name__ == '__main__':
    solve()