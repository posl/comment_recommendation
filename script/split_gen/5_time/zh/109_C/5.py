def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    x_diff = []
    for i in range(n):
        x_diff.append(x_list[i+1]-x_list[i])
    x_diff.sort()
    print(x_diff[0])
