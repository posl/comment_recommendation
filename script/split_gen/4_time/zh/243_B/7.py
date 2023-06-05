def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if a[i] in b_dict.keys() and a[i] == b[i]:
            count_1 += 1
        if a[i] in b_dict.keys() and a[i] != b[i]:
            count_2 += 1
    print(count_1)
    print(count_2)
