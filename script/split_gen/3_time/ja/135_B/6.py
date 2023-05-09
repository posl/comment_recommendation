def main():
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        if i+1 != p[i]:
            for j in range(i+1, n):
                if j+1 == p[i]:
                    p[i], p[j] = p[j], p[i]
                    break
            else:
                print("NO")
                break
    else:
        print("YES")
