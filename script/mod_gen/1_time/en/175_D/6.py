def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # P[i] = P_i - 1
    for i in range(N):
        P[i] -= 1
    # C[i] = C_i
    # C[i] = C_{P_i}
    for i in range(N):
        C[i] = C[P[i]]
    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}}
    for i in range(N):
        C[i] += C[P[i]]
    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}}
    for i in range(N):
        C[i] += C[P[i]]
    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}} + C_{P_{P_{P_{P_{P_{P_i}}}}}}
    for i in range(N):
        C[i] += C[P[i]]
    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}} + C_{P_{P_{P_{P_{P_{P_i}}}}}} + C_{P_{P_{P_{P_{P_{P_{P_i}}}}}}}
    for i in range(N):
        C[i] += C[P[i]]
    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}} + C_{P_{P_{P_{P_{P_{P_i}}}}}} + C_{P_{P_{P_{P_{P_{P_{P_i}}}}}}} + C_{P_{P_{P_{P_{

if __name__ == '__main__':
    main()