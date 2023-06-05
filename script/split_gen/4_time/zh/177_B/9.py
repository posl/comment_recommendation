def main():
    S = input()
    T = input()
    count = 0
    for i in range(len(S)-len(T)+1):
        s = S[i:i+len(T)]
        for j in range(len(T)):
            if s[j] != T[j]:
                count += 1
    print(count)
main()
