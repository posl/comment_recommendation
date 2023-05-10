def main():
    n = int(input())
    a = list(map(int, input().split()))
    # print(n, a)
    a_dict = {}
    for i in range(2**n):
        a_dict[a[i]] = i+1
    # print(a_dict)
    a_sorted = sorted(a_dict.items(), reverse=True)
    # print(a_sorted)
    a_sorted = [i[1] for i in a_sorted]
    # print(a_sorted)
    a_sorted = a_sorted[:2]
    print(min(a_sorted))
