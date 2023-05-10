def main():
    S = input()
    T = input()
    S_dict = {}
    T_dict = {}
    for s in S:
        if s in S_dict:
            S_dict[s] += 1
        else:
            S_dict[s] = 1
    for t in T:
        if t in T_dict:
            T_dict[t] += 1
        else:
            T_dict[t] = 1
    if sorted(S_dict.values()) == sorted(T_dict.values()):
        print("Yes")
    else:
        print("No")
