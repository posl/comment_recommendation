def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    a_count = [0] * n
    for i in range(n):
        a_count[a[i] - 1] += 1
    c_count = [0] * n
    for i in range(n):
        c_count[c[i]] += 1
    count = 0
    for i in range(n):
        count += a_count[i] * c_count[i]
    print(count)
