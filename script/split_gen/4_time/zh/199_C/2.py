def main():
    N = int(input())
    S = input()
    Q = int(input())
    T = [0] * Q
    A = [0] * Q
    B = [0] * Q
    for i in range(Q):
        T[i], A[i], B[i] = map(int, input().split())
    head = S[:N]
    tail = S[N:]
    for i in range(Q):
        if T[i] == 1:
            if A[i] <= N:
                if B[i] <= N:
                    head = head[:A[i]-1] + tail[B[i]-1] + head[A[i]:]
                    tail = tail[:B[i]-1] + head[A[i]-1] + tail[B[i]:]
                else:
                    head = head[:A[i]-1] + tail[B[i]-N-1] + head[A[i]:]
                    tail = tail[:B[i]-N-1] + head[A[i]-1] + tail[B[i]-N:]
            else:
                if B[i] <= N:
                    head = head[:A[i]-N-1] + tail[B[i]-1] + head[A[i]-N:]
                    tail = tail[:B[i]-1] + head[A[i]-N-1] + tail[B[i]:]
                else:
                    head = head[:A[i]-N-1] + tail[B[i]-N-1] + head[A[i]-N:]
                    tail = tail[:B[i]-N-1] + head[A[i]-N-1] + tail[B[i]-N:]
        else:
            head, tail = tail, head
    print(head + tail)
