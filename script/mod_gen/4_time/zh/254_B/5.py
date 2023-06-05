def get_a(i,j):
    if j == 0 or j == i:
        return 1
    else:
        return get_a(i-1,j-1) + get_a(i-1,j)
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(get_a(i,j),end=" ")
    print()

if __name__ == '__main__':
    get_a()