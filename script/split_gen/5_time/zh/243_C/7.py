def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    s = input()
    #print(n)
    #print(x)
    #print(y)
    #print(s)
    for i in range(n):
        if s[i] == 'L':
            x[i] = -x[i]
        elif s[i] == 'R':
            pass
        else:
            print("error")
            return
    #print(x)
    #print(y)
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j]:
                print("Yes")
                return
    print("No")
    return
main()
