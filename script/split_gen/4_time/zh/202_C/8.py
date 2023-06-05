def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    c = list(map(int, input().split(' ')))
    a_dict = {}
    b_dict = {}
    c_dict = {}
    for i in range(n):
        a_dict[a[i]] = a_dict.get(a[i], 0) + 1
        b_dict[b[i]] = b_dict.get(b[i], 0) + 1
        c_dict[c[i]] = c_dict.get(c[i], 0) + 1
    result = 0
    for i in range(1, n + 1):
        if i in c_dict:
            result += a_dict.get(b_dict.get(c_dict[i], 0), 0)
    print(result)
