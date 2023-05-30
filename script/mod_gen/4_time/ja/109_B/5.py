def is_shiritori(N, W):
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            return False
        if W[i] in W[i+1:]:
            return False
    return True
N = int(input())
W = [input() for _ in range(N)]
print('Yes' if is_shiritori(N, W) else 'No')
