Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(1, N):
        if S[i-1] == S[i]:
            ans += 1
    print(min(N-1, ans+2*K))

=======
Suggestion 2

def solve(n, k, s):
    # 0回転のときの幸福数を計算
    cnt = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt += 1

    # 1回転のときの幸福数を計算
    cnt2 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt2 += 1
    cnt2 += 2

    # 2回転のときの幸福数を計算
    cnt3 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt3 += 1
    cnt3 += 4

    # 3回転のときの幸福数を計算
    cnt4 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt4 += 1
    cnt4 += 6

    # 4回転のときの幸福数を計算
    cnt5 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt5 += 1
    cnt5 += 8

    # 5回転のときの幸福数を計算
    cnt6 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt6 += 1
    cnt6 += 10

    # 6回転のときの幸福数を計算
    cnt7 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt7 += 1
    cnt7 += 12

    # 7回転のときの幸福数を計算
    cnt8 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt8 += 1
    cnt8 +=

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    #print(S[0])
    #print(S[-1])
    #print(S[0] == S[-1])
    #print(S[0] == S[-1] == 'L')
    #print(S[0] == S[-1] == 'R')
    #print(S[0] == S[-1] == 'R' or S[0] == S[-1] == 'L')
    #print(S[0] == S[-1] == 'L' or S[0] == S[-1] == 'R')
    #print(S[0] == S[-1] == 'L' or S[0] == S[-1] == 'R' or (S[0] == 'R' and S[-1] == 'L'))
    #print(S[0] == S[-1] == 'L' or S[0] == S[-1] == 'R' or (S[0] == 'R' and S[-1] == 'L') or (S[0] == 'L' and S[-1] == 'R'))
    #print(S[0] == S[-1] == 'L' or S[0] == S[-1] == 'R' or (S[0] == 'R' and S[-1] == 'L') or (S[0] == 'L' and S[-1] == 'R') or (S[0] == S[-1] == 'R' and S[0] == S[-1] == 'L'))
    #print(S[0] == S[-1] == 'L' or S[0] == S[-1] == 'R' or (S[0] == 'R' and S[-1] == 'L') or (S[0] == 'L' and S[-1] == 'R') or (S[0] == S[-1] == 'R' and S[0] == S[-1] == 'L') or (S[0] == S[-1] == 'R' and S[0] == S[-1] == 'R'))
    #print(S[0] == S[-1] == '

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    cnt = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            cnt += 1
    print(min(N-1, cnt+2*K))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans += 1
    ans = min(N-1, ans+2*K)
    print(ans)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt += 1
    ans = min(cnt + 2*K, N-1)
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            cnt += 1
    print(min(N - 1, cnt + 2 * K))
main()

=======
Suggestion 8

def solve(n,k,s):
    ans = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans += 1
    ans += min(2*k, ans+2)
    return ans

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    S = input()
    L = []
    R = []
    for i in range(N):
        if S[i] == "L":
            L.append(i)
        else:
            R.append(i)
    ans = 0
    for i in range(len(L)):
        if i == 0:
            ans += L[i]
        else:
            ans += L[i] - L[i - 1] - 1
    for i in range(len(R)):
        if i == 0:
            ans += R[i]
        else:
            ans += R[i] - R[i - 1] - 1
    ans += len(L) + len(R)
    ans -= 1
    ans = min(ans, N - 1)
    print(ans)

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    S = input()
    #print(N, K, S)
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S[66])
    #print
