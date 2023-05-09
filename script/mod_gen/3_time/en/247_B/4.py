def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    if len(s) == len(set(s)) and len(t) == len(set(t)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()