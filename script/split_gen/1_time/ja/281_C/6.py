def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, T)
    #print(A)
    #print(sum(A))
    #print(T%sum(A))
    #print(T//sum(A))
    #print(N*T//sum(A))
    #print(T%sum(A) + N*T//sum(A))
    #print(T%sum(A) + N*T//sum(A) - N)
    #print((T%sum(A) + N*T//sum(A) - N) % N)
    #print((T%sum(A) + N*T//sum(A) - N) % N + 1)
    #print((T%sum(A) + N*T//sum(A) - N) % N + 1, ((T%sum(A) + N*T//sum(A) - N) // N) % A[(T%sum(A) + N*T//sum(A) - N) % N])
    ans = (T%sum(A) + N*T//sum(A) - N) % N + 1, ((T%sum(A) + N*T//sum(A) - N) // N) % A[(T%sum(A) + N*T//sum(A) - N) % N]
    #print(ans)
    print(*ans)
