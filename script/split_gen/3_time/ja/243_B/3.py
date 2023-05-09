def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dic = {}
    b_dic = {}
    for i in range(n):
        a_dic[a[i]] = i
        b_dic[b[i]] = i
    count = 0
    for i in range(n):
        if a[i] in b_dic:
            if a_dic[a[i]] == b_dic[a[i]]:
                count += 1
    print(count)
    count = 0
    for i in range(n):
        if a[i] in b_dic:
            if a_dic[a[i]] != b_dic[a[i]]:
                count += 1
    print(count)
