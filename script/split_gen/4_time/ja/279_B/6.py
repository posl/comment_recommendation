def main():
    S = input()
    T = input()
    s_len = len(S)
    t_len = len(T)
    if s_len < t_len:
        print("No")
        return
    for i in range(s_len - t_len + 1):
        if S[i:i+t_len] == T:
            print("Yes")
            return
    print("No")
    return
