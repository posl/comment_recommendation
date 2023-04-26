Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    cnt = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                cnt += 1
            if cnt == k:
                print(s[i]+s[j])
                exit()
        cnt += 1
        if cnt == k:
            print(s[i]+s[i])
            exit()

=======
Suggestion 2

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    S = ''.join(S)
    for i in range(K-1):
        S = next_permutation(S)
    print(S)

=======
Suggestion 3

def main():
    S,K = input().split()
    K = int(K)
    #print(S,K)
    S = list(S)
    S.sort()
    #print(S)
    for i in range(K-1):
        S = next_permutation(S)
    print("".join(S))

=======
Suggestion 4

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    ans = []
    while True:
        if len(S) == 0:
            break
        tmp = len(S)
        for i in range(1, len(S)):
            tmp = tmp * i
            if tmp >= K:
                ans.append(S[i-1])
                K = K - (tmp // i)
                S.pop(i-1)
                break
        else:
            ans.append(S[-1])
            S.pop()
    print("".join(ans))

=======
Suggestion 5

def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = ''.join(S)
    S = list(S)
    #print(S)
    #print(K)
    #print(len(S))
    #print(len(S) ** len(S))
    #print(len(S) ** len(S) // len(S))
    #print(len(S) ** len(S) // len(S) // len(S))
    #print(len(S) ** len(S) // len(S) // len(S) // len(S))
    #print(len(S) ** len(S) // len(S) // len(S) // len(S) // len(S))
    #print(len(S) ** len(S) // len(S) // len(S) // len(S) // len(S) // len(S))
    #print(len(S) ** len(S) // len(S) // len(S) // len(S) // len(S) // len(S) // len(S))
    #print(len(S) ** len(S) // len(S) // len(S) // len(S) // len(S) // len(S) // len(S) //

=======
Suggestion 6

def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    L = len(S)
    #print(S)
    #print(L)
    #print(K)
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
    #print(S

=======
Suggestion 7

def getPermutations(S):
    if len(S) == 1:
        return S
    else:
        L = []
        for i in range(len(S)):
            a = S[i]
            b = S[0:i] + S[i+1:]
            for x in getPermutations(b):
                L.append(a + x)
        return L

S, K = input().split()
K = int(K)
L = getPermutations(S)
L.sort()
print(L[K-1])

=======
Suggestion 8

def main():
    S, K = input().split(" ")
    K = int(K)
    print("".join(sorted(S)[K-1]))

main()

=======
Suggestion 9

def main():
    S, K = input().split()
    K = int(K)
    S = sorted(S)
    #print(S)
    N = len(S)
    #print(N)
    #print(K)
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
