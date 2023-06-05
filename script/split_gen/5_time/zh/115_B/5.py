def main():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    p_list.sort(reverse=True)
    p_list[0] = p_list[0] / 2
    print(int(sum(p_list)))
