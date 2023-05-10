def main():
    n = int(input())
    a_list = []
    b_list = []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    b_list.sort(reverse=True)
    b_sum = sum(b_list)
    a_sum = 0
    for i in range(n):
        a_sum += a_list[i]
        if a_sum > b_sum:
            print(i+1)
            exit()
