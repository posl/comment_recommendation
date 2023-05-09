def problem261_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s_dict = {}
    for i in range(n):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
            s[i] = s[i] + "(" + str(s_dict[s[i]]) + ")"
        else:
            s_dict[s[i]] = 0
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    problem261_c()