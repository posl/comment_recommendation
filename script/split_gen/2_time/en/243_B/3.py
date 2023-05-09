def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {}
    b_dict = {}
    for i in range(n):
        a_dict[a[i]] = i
        b_dict[b[i]] = i
    same = 0
    diff = 0
    for i in range(n):
        if a[i] in b_dict.keys():
            if a_dict[a[i]] == b_dict[a[i]]:
                same += 1
            else:
                diff += 1
    print(same)
    print(diff)
