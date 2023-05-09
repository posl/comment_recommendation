def main():
    S = input()
    T = input()
    for x in range(len(T)+1):
        S_prime = S[:x] + S[-(len(T)-x):]
        match = True
        for i in range(len(T)):
            if S_prime[i] != T[i] and S_prime[i] != "?":
                match = False
                break
        if match:
            print("Yes")
        else:
            print("No")
