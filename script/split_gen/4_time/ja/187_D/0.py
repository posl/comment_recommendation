def main():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    a_list.sort(reverse=True)
    b_list.sort(reverse=True)
    a_total = sum(a_list)
    b_total = sum(b_list)
    a_count = 0
    b_count = 0
    for a, b in zip(a_list, b_list):
        a_count += a
        b_count += b
        if b_count > a_total - a_count:
            print(n - a_list.index(a))
            break
    else:
        print(0)
