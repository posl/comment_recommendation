def main():
    n = int(input())
    v = list(map(int, input().split()))
    if n % 2 == 0:
        even_list = v[::2]
        odd_list = v[1::2]
        even_list_1 = sorted(even_list)
        odd_list_1 = sorted(odd_list)
        if even_list_1[0] == even_list_1[-1] and odd_list_1[0] == odd_list_1[-1]:
            print(n // 2)
        elif even_list_1[0] == even_list_1[-1] and odd_list_1[0] != odd_list_1[-1]:
            print(n // 2 - odd_list.count(odd_list_1[-1]))
        elif even_list_1[0] != even_list_1[-1] and odd_list_1[0] == odd_list_1[-1]:
            print(n // 2 - even_list.count(even_list_1[-1]))
        else:
            print(n // 2 - even_list.count(even_list_1[-1]) - odd_list.count(odd_list_1[-1]))
    else:
        print("n is not even")
