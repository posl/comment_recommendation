def main():
    N, A, B = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(N//2):
        if S[i] != S[N-i-1]:
            if S[i] == 'a' and S[N-i-1] == 'b':
                cnt += A
            elif S[i] == 'b' and S[N-i-1] == 'a':
                cnt += A
            elif S[i] == 'c' and S[N-i-1] == 'd':
                cnt += A
            elif S[i] == 'd' and S[N-i-1] == 'c':
                cnt += A
            elif S[i] == 'e' and S[N-i-1] == 'f':
                cnt += A
            elif S[i] == 'f' and S[N-i-1] == 'e':
                cnt += A
            elif S[i] == 'g' and S[N-i-1] == 'h':
                cnt += A
            elif S[i] == 'h' and S[N-i-1] == 'g':
                cnt += A
            elif S[i] == 'i' and S[N-i-1] == 'j':
                cnt += A
            elif S[i] == 'j' and S[N-i-1] == 'i':
                cnt += A
            elif S[i] == 'k' and S[N-i-1] == 'l':
                cnt += A
            elif S[i] == 'l' and S[N-i-1] == 'k':
                cnt += A
            elif S[i] == 'm' and S[N-i-1] == 'n':
                cnt += A
            elif S[i] == 'n' and S[N-i-1] == 'm':
                cnt += A
            elif S[i] == 'o' and S[N-i-1] == 'p':
                cnt += A
            elif S[i] == 'p' and S[N-i-1] == 'o':
                cnt += A
            elif S[i] == 'q' and S[N-i-1] == 'r':
                cnt += A
            elif S[i] == 'r' and S[N-i-1] == 'q':
                cnt += A
            elif
