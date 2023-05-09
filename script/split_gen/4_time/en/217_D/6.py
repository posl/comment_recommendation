def main():
    L,Q = map(int, input().split())
    cut = [0 for _ in range(L)]
    cut[0] = 1
    cut[L-1] = 1
    for _ in range(Q):
        c,x = map(int, input().split())
        if c == 1:
            cut[x-1] = 1
        else:
            left = x-1
            right = x-1
            while left >= 0 and cut[left] == 0:
                left -= 1
            while right < L and cut[right] == 0:
                right += 1
            print(right-left)
