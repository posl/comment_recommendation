def main():
    n = int(input())
    heights = [int(i) for i in input().split()]
    for i in range(n-1):
        if heights[i] > heights[i+1]:
            heights[i] -= 1
    for i in range(n-1):
        if heights[i] > heights[i+1]:
            print("No")
            return
    print("Yes")
    return
