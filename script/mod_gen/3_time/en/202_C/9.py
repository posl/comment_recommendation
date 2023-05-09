def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_dict = {}
    for i in range(N):
        b = B[i]
        if b in B_dict:
            B_dict[b].append(i)
        else:
            B_dict[b] = [i]
    C_dict = {}
    for i in range(N):
        c = C[i]
        if c in C_dict:
            C_dict[c].append(i)
        else:
            C_dict[c] = [i]
    count = 0
    for a in A:
        if a in B_dict:
            for b_i in B_dict[a]:
                if C[b_i] in C_dict:
                    count += len(C_dict[C[b_i]])
    return count
print(solve())

if __name__ == '__main__':
    solve()