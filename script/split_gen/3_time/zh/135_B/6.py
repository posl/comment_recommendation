def main():
    N = int(input())
    p = list(map(int, input().split()))
    is_sorted = True
    for i in range(N-1):
        if p[i] > p[i+1]:
            is_sorted = False
            break
    if is_sorted:
        print("YES")
    else:
        print("NO")
