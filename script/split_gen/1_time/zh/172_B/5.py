def main():
    S = input()
    T = input()
    if S == T:
        print(0)
        return
    else:
        count = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                count += 1
        print(count)
