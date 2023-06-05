def main():
    n = int(input())
    p_list = [int(input()) for i in range(n)]
    p_list.sort(reverse=True)
    p_list[0] = p_list[0] // 2
    print(sum(p_list))
    return
