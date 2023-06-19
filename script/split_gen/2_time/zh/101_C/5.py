def main():
    n, k = map(int, input().split())
    a_list = [int(i) for i in input().split()]
    a_list_sorted = sorted(a_list)
    a_list_sorted = a_list_sorted[::-1]
    a_list_sorted = a_list_sorted[:n-k]
    print(sum(a_list_sorted))
