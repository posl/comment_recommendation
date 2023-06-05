def find_min_operation(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return min(find_min_operation(N-1)+1,find_min_operation(N-6**2)+1,find_min_operation(N-9**2)+1)
N = int(input())
print(find_min_operation(N))
