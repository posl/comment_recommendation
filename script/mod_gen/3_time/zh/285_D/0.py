def handle_change():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i] == t[j] and s[j] == t[i]:
                return "Yes"
    return "No"

if __name__ == '__main__':
    handle_change()