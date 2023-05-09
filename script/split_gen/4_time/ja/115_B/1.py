def main():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    p_list.sort()
    p_list[n-1] = int(p_list[n-1]/2)
    print(sum(p_list))
