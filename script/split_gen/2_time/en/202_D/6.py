def main():
    A, B, K = map(int, input().split())
    s = A + B
    ans = ''
    for i in range(s):
        if A == 0:
            ans += 'b'
            B -= 1
        elif B == 0:
            ans += 'a'
            A -= 1
        elif K <= comb(A + B - 1, B):
            ans += 'a'
            A -= 1
        else:
            ans += 'b'
            K -= comb(A + B - 1, B)
            B -= 1
    print(ans)
