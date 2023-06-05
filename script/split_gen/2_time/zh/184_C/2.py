def problem184_b():
    n,x = map(int,input().split())
    s = input()
    result = x
    for i in range(n):
        if s[i] == 'o':
            result += 1
        elif s[i] == 'x':
            if result > 0:
                result -= 1
    print(result)
