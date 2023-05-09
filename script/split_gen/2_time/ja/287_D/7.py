def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_ = S[:i] + S[-(len(T)-i):]
        if S_.count("?") + S_.count(T) == len(S_):
            print("Yes")
        else:
            print("No")
