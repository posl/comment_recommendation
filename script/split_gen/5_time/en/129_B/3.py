def main():
    n = int(input())
    w = list(map(int, input().split()))
    w_sum = sum(w)
    for i in range(n):
        s1 = sum(w[:i+1])
        s2 = w_sum - s1
        print(abs(s1 - s2))
    return
