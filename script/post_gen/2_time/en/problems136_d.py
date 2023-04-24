Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    L[0] = 1
    R[-1] = 1
    for i in range(1, N):
        if S[i-1] == "L":
            L[i] = L[i-1] + 1
        else:
            L[i] = L[i-1]
    for i in range(N-2, -1, -1):
        if S[i] == "R":
            R[i] = R[i+1] + 1
        else:
            R[i] = R[i+1]
    for i in range(N):
        print((L[i] + R[i]) // 2, end=" ")
    print()

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == 'L':
            L[i] = 1
        else:
            R[i] = 1
    for i in range(1, N):
        L[i] += L[i - 1]
    for i in reversed(range(N - 1)):
        R[i] += R[i + 1]
    for i in range(N):
        if S[i] == 'L':
            print((R[i] + 1) // 2, end=' ')
        else:
            print((L[i] + 1) // 2, end=' ')
    print()

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    L = [0] * N
    R = [0] * N
    for i in range(N):
        if S[i] == "R":
            R[i] = 1
        else:
            L[i] = 1
    for i in range(N):
        if i > 0:
            L[i] += L[i - 1]
    for i in range(N - 1, -1, -1):
        if i < N - 1:
            R[i] += R[i + 1]
    ans = []
    for i in range(N):
        if S[i] == "R":
            ans.append(L[i] + R[i + 1] - 1)
        else:
            ans.append(L[i - 1] + R[i] - 1)
    print(" ".join(map(str, ans)))

=======
Suggestion 4

def main():
    S = input()
    N = len(S)
    L = [0 for _ in range(N+1)]
    R = [0 for _ in range(N+1)]
    for i in range(N):
        if S[i] == 'L':
            L[i+1] = L[i] + 1
        else:
            R[i+1] = R[i] + 1
    ans = [0 for _ in range(N)]
    for i in range(N):
        if S[i] == 'L':
            ans[i] += R[i] + 1 - (L[i] + 1) // 2
            ans[i-1] += (L[i] + 1) // 2
        else:
            ans[i] += L[i+1] - R[i] // 2
            ans[i+1] += R[i] // 2
    print(*ans)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    count = 0
    for i in range(N):
        if S[i] == 'R':
            count += 1
        else:
            ans[i] += count // 2
            ans[i-1] += (count + 1) // 2
            count = 0
    count = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            count += 1
        else:
            ans[i] += count // 2
            ans[i+1] += (count + 1) // 2
            count = 0
    print(*ans)

main()

=======
Suggestion 6

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[N - 1] = 1
    for i in range(1, N - 1):
        if S[i] == "L":
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1] - 1
    for i in range(N - 2, -1, -1):
        if S[i] == "R":
            ans[i] = ans[i + 1] + 1
        else:
            ans[i] = ans[i + 1] - 1
    print(*ans)

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[-1] = 1
    for i in range(1, N-1):
        if S[i] == "L":
            ans[i-1] += 1
        else:
            ans[i+1] += 1

    print(" ".join(map(str, ans)))

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    a = [0] * n
    b = [0] * n
    for i in range(n):
        if s[i] == 'R':
            a[i] += 1
            b[i+1] -= 1
        else:
            b[i] += 1
            a[i-1] -= 1
    for i in range(n):
        a[i+1] += a[i]
        b[i+1] += b[i]
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] + b[i]
    print(*ans)

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    #print(N)
    #print(S)
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
    #print(S[67])

=======
Suggestion 10

def main():
    S = input()
    N = len(S)

    # 1. Find the first 'L'
    # 2. Find the first 'R' after the 'L'
    # 3. If the number of 'R's is odd, distribute the number of 'R's to the left and right of the 'L'
    # 4. If the number of 'R's is even, distribute the number of 'R's to the left and right of the 'L' equally

    # 1. Find the first 'L'
    # 2. Find the first 'R' after the 'L'
    # 3. If the number of 'R's is odd, distribute the number of 'R's to the left and right of the 'L'
    # 4. If the number of 'R's is even, distribute the number of 'R's to the left and right of the 'L' equally

    # 1. Find the first 'L'
    # 2. Find the first 'R' after the 'L'
    # 3. If the number of 'R's is odd, distribute the number of 'R's to the left and right of the 'L'
    # 4. If the number of 'R's is even, distribute the number of 'R's to the left and right of the 'L' equally

    # 1. Find the first 'L'
    # 2. Find the first 'R' after the 'L'
    # 3. If the number of 'R's is odd, distribute the number of 'R's to the left and right of the 'L'
    # 4. If the number of 'R's is even, distribute the number of 'R's to the left and right of the 'L' equally

    # 1. Find the first 'L'
    # 2. Find the first 'R' after the 'L'
    # 3. If the number of 'R's is odd, distribute the number of 'R's to the left and right of the 'L'
    # 4. If the number of 'R's is even, distribute the number of 'R's to the left and right of the 'L' equally

    # 1. Find the first 'L'
    # 2. Find the first 'R'
