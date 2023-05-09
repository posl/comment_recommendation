def check_sort(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True
N = int(input())
p_list = list(map(int, input().split()))
for i in range(N):
    for j in range(i+1, N):
        p_list[i], p_list[j] = p_list[j], p_list[i]
        if check_sort(p_list):
            print("YES")
            exit()
        p_list[i], p_list[j] = p_list[j], p_list[i]
print("NO")

if __name__ == '__main__':
    check_sort()