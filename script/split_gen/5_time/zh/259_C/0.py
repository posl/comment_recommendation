def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) < len(T):
        print("No")
        return
    if len(S) == len(T):
        print("Yes")
        return
    #S长度大于T
    #S中是否存在T的子串
    if T in S:
        print(
