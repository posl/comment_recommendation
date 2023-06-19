def problem187_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    for i in range(n):
        if s[i][0] == "!":
            if s[i][1:] in s:
                print(s[i][1:])
                break
        else:
            if "!" + s[i] in s:
                print(s[i])
                break
    else:
        print("satisfiable")
