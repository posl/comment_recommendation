def find_ocean_inns():
    n = int(input())
    H = list(map(int, input().split()))
    ocean_inns = 1
    for i in range(1, n):
        if max(H[:i]) <= H[i]:
            ocean_inns += 1
    return ocean_inns
print(find_ocean_inns())

if __name__ == '__main__':
    find_ocean_inns()