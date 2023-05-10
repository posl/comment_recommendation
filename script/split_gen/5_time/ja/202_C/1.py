def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    c_dict = {}
    for c in c_list:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1
    b_dict = {}
    for b in b_list:
        if b in b_dict:
            b_dict[b] += 1
        else:
            b_dict[b] = 1
    a_dict = {}
    for a in a_list:
        if a in a_dict:
            a_dict[a] += 1
        else:
            a_dict[a] = 1
    ans = 0
    for i in range(1, n + 1):
        if i in a_dict and i in b_dict:
            ans += a_dict[i] * b_dict[i] * c_dict[i]
    print(ans)
