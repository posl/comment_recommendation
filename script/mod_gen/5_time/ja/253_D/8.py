def problem253_d():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    #print((N // A) * A, (N // B) * B)
    #print((N // A) * A + (N // B) * B)
    #print((N // A) * A + (N // B) * B - (N // (A*B)) * (A*B))
    print(N * (N + 1) // 2 - (N // A) * (A * (1 + N // A)) // 2 - (N // B) * (B * (1 + N // B)) // 2 + (N // (A * B)) * ((A * B) * (1 + N // (A * B))) // 2)

if __name__ == '__main__':
    problem253_d()