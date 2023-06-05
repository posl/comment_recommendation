def main():
    # input
    n = int(input())
    a_list = list(map(int, input().split()))
    # solve
    ans = 0
    d = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a_list[j] == 0:
                continue
            if a_list[i] % a_list[j] != 0:
                continue
            if a_list[i] // a_list[j] in d:
                ans += d[a_list[i] // a_list[j]]
    # output
    print(ans)
