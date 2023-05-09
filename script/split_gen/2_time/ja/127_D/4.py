def main():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    bc_list = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc_list.append((b, c))
    a_list.sort(reverse=True)
    bc_list.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a_list[i] < bc_list[j][1]:
            a_list[i] = bc_list[j][1]
            bc_list[j] = (bc_list[j][0] - 1, bc_list[j][1])
            if bc_list[j][0] == 0:
                j += 1
        else:
            break
        i += 1
    print(sum(a_list))
