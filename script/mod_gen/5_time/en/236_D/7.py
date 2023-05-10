def calc_xor(list1):
    xor = 0
    for i in list1:
        xor = xor ^ i
    return xor
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
max_xor = 0
for i in range(2**N):
    pair_list = []
    for j in range(N):
        if (i >> j) & 1 == 1:
            pair_list.append(j)
    if len(pair_list) == 2:
        max_xor = max(max_xor, A[pair_list[0]][pair_list[1]])
    elif len(pair_list) > 2:
        xor_list = []
        for k in range(len(pair_list)-1):
            xor_list.append(A[pair_list[k]][pair_list[k+1]])
        max_xor = max(max_xor, calc_xor(xor_list))
print(max_xor)

if __name__ == '__main__':
    calc_xor()