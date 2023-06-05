def find_pairs(A, B, C):
    A = [a-1 for a in A]
    B = [b-1 for b in B]
    C = [c-1 for c in C]
    #print(A, B, C)
    C_dict = {}
    for i, c in enumerate(C):
        if c not in C_dict:
            C_dict[c] = []
        C_dict[c].append(i)
    #print(C_dict)
    count = 0
    for i, a in enumerate(A):
        if B[a] in C_dict:
            count += len(C_dict[B[a]])
    return count

if __name__ == '__main__':
    find_pairs()