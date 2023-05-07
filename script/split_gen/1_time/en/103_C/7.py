def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    max_a = a_list[-1]
    a_list.pop()
    a_list.reverse()
    max_sum = 0
    for i in range(n-1):
        max_sum += max_a % a_list[i]
    print(max_sum)
