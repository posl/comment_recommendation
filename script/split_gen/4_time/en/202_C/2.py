def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(B)
    #print(C)
    # create a dictionary with keys as the values in C and values as the count of each value
    C_dict = {}
    for c in C:
        if c in C_dict:
            C_dict[c] += 1
        else:
            C_dict[c] = 1
    #print(C_dict)
    # create a dictionary with keys as the values in B and values as the count of each value
    B_dict = {}
    for b in B:
        if b in B_dict:
            B_dict[b] += 1
        else:
            B_dict[b] = 1
    #print(B_dict)
    # create a dictionary with keys as the values in A and values as the count of each value
    A_dict = {}
    for a in A:
        if a in A_dict:
            A_dict[a] += 1
        else:
            A_dict[a] = 1
    #print(A_dict)
    count = 0
    for key in C_dict.keys():
        if key in B_dict.keys():
            count += C_dict[key] * B_dict[key]
    print(count)
