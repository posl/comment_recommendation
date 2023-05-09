def main():
    S = input()
    N = len(S)
    result = [0]*N
    R = 0
    L = 0
    for i in range(N):
        if S[i] == 'R':
            R += 1
        else:
            L += 1
        if S[i] == 'R' and S[i+1] == 'L':
            result[i] += R//2
            result[i+1] += (R+1)//2
            R = 0
        if S[i] == 'L' and S[i+1] == 'R':
            result[i-1] += (L+1)//2
            result[i] += L//2
            L = 0
    print(*result)
