def cal_energy(A, B):
    return 32 ** (A-B)
A, B = map(int, input().split())
print(cal_energy(A, B))
