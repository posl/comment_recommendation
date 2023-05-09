def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    a_count = [0] * 100001
    c_count = [0] * 100001
    for i in range(n):
        a_count[a_list[i]] += 1
        c_count[c_list[i]] += 1
    b_count = [0] * 100001
    for i in range(n):
        b_count[b_list[c_list[i] - 1]] += 1
    ans = 0
    for i in range(100001):
        ans += a_count[i] * b_count[i]
    print(ans)
