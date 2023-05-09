def main():
    S = input()
    T = input()
    S_list = list(S)
    T_list = list(T)
    S_list.sort()
    T_list.sort(reverse=True)
    if S_list < T_list:
        print("Yes")
    else:
        print("No")
