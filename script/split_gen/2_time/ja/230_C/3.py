def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    #print(N, A, B, P, Q, R, S)
    #N, A, B, P, Q, R, S = 5, 3, 2, 1, 5, 1, 5
    #N, A, B, P, Q, R, S = 5, 3, 3, 4, 5, 2, 5
    #N, A, B, P, Q, R, S = 1000000000000000000, 999999999999999999, 999999999999999999, 999999999999999998, 1000000000000000000, 999999999999999998, 1000000000000000000
    #print(N, A, B, P, Q, R, S)
    #max(1-A,1-B)≦ k≦ min(N-A,N-B) をみたす全ての整数 k について、(A+k,B+k) を黒く塗る。
    #max(1-A,B-N)≦ k≦ min(N-A,B-1) をみたす全ての整数 k について、(A+k,B-k) を黒く塗る。
    #print(P, Q, R, S)
    #print(1-A, 1-B, N-A, N-B)
    #print(1-A, B-N, N-A, B-1)
    #print(max(1-A,1-B), min(N-A,N-B))
    #print(max(1-A,B-N), min(N-A,B-1))
    #print(max(1-A,1-B) <= min(N-A,N-B))
    #print(max(1-A,B-N) <= min(N-A,B-1))
    #print(max(1-A,1-B) <= min(N-A,N-B) and max(1-A,B-N) <= min(N-A,B-1))
    #print(max(1-A,1-B) <= min(N-A,N-B) and max(1-A,B-N) <= min(N-A,B-1)
