def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    same_pos = 0
    diff_pos = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] == b_dict[a[i]]:
                same_pos += 1
            else:
                diff_pos += 1
    print(same_pos)
    print(diff_pos)
