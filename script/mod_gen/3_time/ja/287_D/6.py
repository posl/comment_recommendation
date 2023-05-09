def main():
    S = input()
    T = input()
    for i in range(len(T)+1):
        S_prime = S[0:i] + S[-(len(T)-i):]
        flag = True
        for j in range(len(T)):
            if S_prime[j] == T[j] or S_prime[j] == "?" or T[j] == "?":
                continue
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()