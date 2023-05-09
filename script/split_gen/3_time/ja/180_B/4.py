def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    x_list = [abs(x) for x in x_list]
    print(sum(x_list))
    print(sum([x**2 for x in x_list])**0.5)
    print(max(x_list))
