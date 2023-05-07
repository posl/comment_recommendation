def main():
    S = input()
    T = input()
    for i in range(len(S)+1):
        if S[:i]+S[i:] == T:
            print(i+1)
            break
