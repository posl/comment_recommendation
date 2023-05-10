def main():
    N = int(input())
    uvw_list = []
    for i in range(N-1):
        uvw_list.append(list(map(int, input().split())))
    print(uvw_list)
