def main():
    N = int(input())
    name = []
    height = []
    for i in range(N):
        name.append(input().split()[0])
        height.append(int(input().split()[1]))
    #print(name)
    #print(height)
    max1 = max(height)
    #print(max1)
    max1_index = height.index(max1)
    #print(max1_index)
    del height[max1_index]
    max2 = max(height)
    #print(max2)
    max2_index = height.index(max2)
    #print(max2_index)
    print(name[max2_index])
