def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(len(x_list)-1):
        diff_list.append(x_list[i+1]-x_list[i])
    diff_list.sort()
    if len(diff_list) == 1:
        print(diff_list[0])
    else:
        gcd = diff_list[0]
        for i in range(1, len(diff_list)):
            gcd = euclid(gcd, diff_list[i])
        print(gcd)
