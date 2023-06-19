def find_price(A, B):
    for i in range(100):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            return i
    return -1
A, B = map(int, input().split())
print(find_price(A, B))
