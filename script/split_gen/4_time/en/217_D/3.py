def main():
    L, Q = map(int, input().split())
    cuts = []
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cuts.append(x)
        else:
            cuts.sort()
            left = 0
            right = len(cuts)
            while left < right:
                mid = (left + right) // 2
                if cuts[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            if left % 2 == 0:
                print(x - cuts[left - 1])
            else:
                print(cuts[left] - x)
