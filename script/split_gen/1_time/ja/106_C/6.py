def main():
    S = input()
    K = int(input())
    ans = ""
    for i in range(K):
        ans += S[i%len(S)]
        if ans[-1] != "1":
            print(ans[-1])
            break
    else:
        print(1)
