def main():
    S = input()
    T = input()
    for i in range(len(T) + 1):
        s = S[:i] + S[-(len(T) - i):]
        if s.replace("?", "") == T:
            print("Yes")
        else:
            print("No")
