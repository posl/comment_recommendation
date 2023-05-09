def harvest():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    a_list = [a for a in a_list if a > 10]
    return sum(a_list) - len(a_list) * 10
print(harvest())
