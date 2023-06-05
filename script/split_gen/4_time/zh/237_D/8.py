def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(1, N):
        if S[i-1] == 'L':
            A.insert(0, i)
        else:
            A.append(i)
    for i in range(N):
        print(A[i], end=' ')
    print(A[N])
