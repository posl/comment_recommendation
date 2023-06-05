def main():
    S = input()
    K = int(input())
    i = 0
    while i < K:
        if S[i] == "1":
            i += 1
        else:
            print(S[i])
            break
    else:
        print("1")
