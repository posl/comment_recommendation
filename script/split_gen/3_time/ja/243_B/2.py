def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_dict = {a[i]: i for i in range(n)}
    b_dict = {b[i]: i for i in range(n)}
    count = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] == b_dict[a[i]]:
                count += 1
    print(count)
    count = 0
    for i in range(n):
        if a[i] in b_dict:
            if a_dict[a[i]] != b_dict[a[i]]:
                count += 1
    print(count)
