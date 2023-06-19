def main():
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)-len(T)+1):
        tmp = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp += 1
        if cnt < tmp:
            cnt = tmp
    print(cnt)
main()
