def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
            cut.sort()
        else:
            left = 0
            right = len(cut) - 1
            while right - left > 1:
                mid = (left + right) // 2
                if cut[mid] > x:
                    right = mid
                else:
                    left = mid
            print(cut[right] - cut[left])
