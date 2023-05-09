def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        else:
            x = query[1]
            k = query[2]
            B = [a for a in A if a <= x]
            B.sort(reverse=True)
            if len(B) < k:
                ans.append(-1)
            else:
                ans.append(B[k-1])
    print(*ans, sep='
')
