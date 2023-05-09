def flip(s):
    return s[N:] + s[:N]
N = int(input())
S = input()
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
for q in query:
    if q[0] == 1:
        A, B = q[1]-1, q[2]-1
        S = S[:A] + S[B] + S[A+1:B] + S[A] + S[B+1:]
    else:
        S = flip(S)
print(S)

if __name__ == '__main__':
    flip()