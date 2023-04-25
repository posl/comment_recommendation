Synthesizing 1/10 solutions

=======
Suggestion 1

def check_match(B, A):
    for i in range(len(A)-len(B)+1):
        for j in range(len(A[0])-len(B[0])+1):
            match = True
            for k in range(len(B)):
                for l in range(len(B[0])):
                    if B[k][l] != A[i+k][j+l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

N, M = map(int, input().split())
B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

A = [[0 for _ in range(7)] for _ in ra
