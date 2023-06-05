def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l_max = max(l)
    l_sum = sum(l) - l_max
    if l_max < l_sum:
        print("是")
    else:
        print("否")
