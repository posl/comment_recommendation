def replace(S):
    S = S.replace('A', 'BC')
    S = S.replace('B', 'CA')
    S = S.replace('C', 'AB')
    return S
S = input()
Q = int(input())
query = []
for _ in range(Q):
    t, k = map(int, input().split())
    query.append((t, k))
for t, k in query:
    if t == 0:
        print(S[k-1])
    else:
        S = replace(S)
        print(S[k-1])

if __name__ == '__main__':
    replace()