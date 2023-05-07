def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dic = {a[i]: i for i in range(n)}
    b_dic = {b[i]: i for i in range(n)}
    count1 = 0
    count2 = 0
    for i in range(n):
        if a[i] in b_dic:
            if a_dic[a[i]] == b_dic[a[i]]:
                count1 += 1
            else:
                count2 += 1
    print(count1)
    print(count2)
