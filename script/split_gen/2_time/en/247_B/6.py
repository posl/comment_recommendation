def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    dict = {}
    for i in range(N):
        dict[s[i]] = i
        dict[t[i]] = i
    if len(dict) == 2*N:
        print("Yes")
    else:
        print("No")
