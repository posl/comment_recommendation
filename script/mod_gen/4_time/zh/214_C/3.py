def main():
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    #print(s)
    #print(t)
    if n == 1:
        print(t[0])
        return
    for i in range(n):
        if i == 0:
            if t[i] < s[i]:
                print(t[i])
            else:
                print(t[i]+s[i])
        else:
            if t[i] < s[i]:
                print(t[i])
            else:
                if t[i] == t[i-1]:
                    print(t[i]+s[i])
                else:
                    print(t[i] + s[i] - t[i-1])
    return
main()
