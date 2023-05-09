def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S1 = S[:i]
        S2 = S[-(len(T)-i):]
        if all([s1 == t1 or s1 == "?" or t1 == "?" for s1, t1 in zip(S1, T[:i])]) and all([s2 == t2 or s2 == "?" or t2 == "?" for s2, t2 in zip(S2, T[i:])]):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()