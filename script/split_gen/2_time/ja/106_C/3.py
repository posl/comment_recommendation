def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] == "1":
            continue
        else:
            print(S[i])
            break
    else:
        print(1)
