def main():
    S = list(input())
    T = list(input())
    for i in range(len(S)):
        if S[i] != T[i]:
            if ord(S[i]) + (len(S) - i) != ord(T[i]):
                print("No")
                return
    print("Yes")
