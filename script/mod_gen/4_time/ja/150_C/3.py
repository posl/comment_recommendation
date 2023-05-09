def permutation(n):
    if n == 1:
        return [[1]]
    else:
        result = []
        for p in permutation(n-1):
            for i in range(n):
                result.append(p[:i] + [n] + p[i:])
        return result
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
p_list = permutation(n)
p_list.sort()
p_index = p_list.index(p)
q_index = p_list.index(q)
print(abs(p_index - q_index))

if __name__ == '__main__':
    permutation()