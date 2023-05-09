def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    if len(set(s)) == len(set(t)) == len(set(s + t)):
        print("Yes")
    else:
        print("No")
