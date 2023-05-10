def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i+1
        b_dict[b[i]] = i+1
    a_set = set(a)
    b_set = set(b)
    a_and_b = a_set & b_set
    a_and_b_dict = {}
    for x in a_and_b:
        a_and_b_dict[x] = [a_dict[x], b_dict[x]]
    cnt1 = 0
    cnt2 = 0
    for x in a_and_b_dict:
        if a_and_b_dict[x][0] == a_and_b_dict[x][1]:
            cnt1 += 1
        else:
            cnt2 += 1
    print(cnt1)
    print(cnt2)
