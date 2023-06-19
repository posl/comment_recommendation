def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    
    s_dict = {}
    t_dict = {}
    for s, t in zip(S, T):
        if s not in s_dict:
            s_dict[s] = t
        else:
            if s_dict[s] != t:
                print("No")
                return
        if t not in t_dict:
            t_dict[t] = s
        else:
            if t_dict[t] != s:
                print("No")
                return
    print("Yes")
    return

if __name__ == '__main__':
    main()