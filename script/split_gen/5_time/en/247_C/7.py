def get_sequence(n):
    if n == 1:
        return [1]
    else:
        seq = get_sequence(n-1)
        return seq + [n] + seq
n = int(input())
for i in get_sequence(n):
    print(i, end=" ")
