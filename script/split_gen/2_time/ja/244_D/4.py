def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
        return
    for i in range(3):
        for j in range(i+1, 3):
            S[i], S[j] = S[j], S[i]
            if S == T:
                print("Yes")
                return
            S[i], S[j] = S[j], S[i]
    print("No")
    return
