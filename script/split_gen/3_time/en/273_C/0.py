def main():
    N = int(input())
    A = list(map(int, input().split()))
    A2 = list(set(A))
    A2.sort()
    d = {}
    for i, a in enumerate(A2):
        d[a] = i
    B = [d[a] for a in A]
    #print(B)
    BIT = BinaryIndexedTree(N)
    BIT.add(B[0], 1)
    ans = []
    for i, b in enumerate(B[1:], 1):
        BIT.add(b, 1)
        #print(b, BIT.sum(0, b), i+1-BIT.sum(0, b))
        ans.append(i+1-BIT.sum(0, b))
    print('
'.join(map(str, ans)))
