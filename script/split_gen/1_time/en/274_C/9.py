def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1から出発するとすると、
    # 2^0, 2^1, 2^2, ... 2^N-1, 2^N, 2^N+1
    # つまり、N+2個の要素を持つリストを作る
    # 0, 1, 2, ... N-1, N, N+1
    # 2^0, 2^1, 2^2, ... 2^N-1, 2^N, 2^N+1
    # と、
    # 1, 2, 3, ... N, N+1, N+2
    # は、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
    # と、
    # 1, 2, 3, ... N, N+1, N+2
    # が等しいことに注意
    # つまり、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
    # と、
    # 1, 2, 3, ... N, N+1, N+2
    # から、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
    # と、
    # 0, 1, 2, ... N-1, N, N+1
    # が等しいことになる
    # つまり、
    # 1, 2, 3, ... N, N+1, N+2
    # と、
    # 0, 1, 2, ... N-1, N, N+1
    # の差分が、
    # 1, 2, 4, ... 2^N, 2^N+1, 2^N+2
