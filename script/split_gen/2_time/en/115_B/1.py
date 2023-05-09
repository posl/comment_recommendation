def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort()
    total = 0
    for i in range(N):
        if i == N-1:
            total += p_list[i]//2
        else:
            total += p_list[i]
    print(total)
