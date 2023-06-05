def main():
    n,x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    distance_list = []
    for i in range(n):
        distance_list.append(x_list[i+1]-x_list[i])
    import math
    print(math.gcd(*distance_list))
main()
