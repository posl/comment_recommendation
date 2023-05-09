def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort()
    p_list[-1] /= 2
    print(int(sum(p_list)))
