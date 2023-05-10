def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    count = min(count+2*K,len(S)-1)
    print(count)
main()
