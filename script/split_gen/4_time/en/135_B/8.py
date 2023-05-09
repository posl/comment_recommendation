def main():
    N = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    if p_sorted == p:
        print("YES")
    else:
        for i in range(N):
            for j in range(i + 1, N):
                p_swapped = p[:]
                p_swapped[i], p_swapped[j] = p_swapped[j], p_swapped[i]
                if p_swapped == p_sorted:
                    print("YES")
                    return
        print("NO")
