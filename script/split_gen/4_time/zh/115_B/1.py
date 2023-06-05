def main():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    p_list.sort()
    p_list[-1] = p_list[-1] // 2
    print(sum(p_list))
