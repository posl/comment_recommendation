def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1,N):
        if S[i-1] == 'L' and S[i] == 'R':
            A.append(i)
        elif S[i-1] == 'R' and S[i] == 'L':
            A.append(i)
    A.append(N)
    for i in range(N):
        print(A[i+1]-A[i],end=' ')
    print()
