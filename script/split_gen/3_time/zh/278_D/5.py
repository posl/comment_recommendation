def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        s = input().split()
        if s[0] == '1':
            x = int(s[1])
            for j in range(N):
                A[j] = x
        elif s[0] == '2':
            i = int(s[1]) - 1
            x = int(s[2])
            A[i] += x
        else:
            i = int(s[1]) - 1
            print(A[i])
