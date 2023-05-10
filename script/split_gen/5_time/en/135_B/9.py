def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    p = [0] + p
    for i in range(1, N):
        if p[i] > p[i+1]:
            for j in range(i+1, N+1):
                if p[i] > p[j]:
                    print("NO")
                    return
            print("YES")
            return
    print("YES")
    return
