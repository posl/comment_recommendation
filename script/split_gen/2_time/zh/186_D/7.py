def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]
    a_list.sort()
    sum = 0
    for i in range(n):
        sum += a_list[i] * (n-i-1) - a_list[i] * i
    print(sum)
