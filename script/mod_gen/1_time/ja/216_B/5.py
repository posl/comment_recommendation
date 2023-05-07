def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = map(str, input().split())
        s.append(s_i)
        t.append(t_i)
    
    if len(s) != len(set(s)) or len(t) != len(set(t)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()