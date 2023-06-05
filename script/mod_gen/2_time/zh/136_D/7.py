def main():
    n = int(input())
    heights = input().split()
    heights = [int(height) for height in heights]
    for i in range(1,n):
        if heights[i] - heights[i-1] > 1:
            print("No")
            exit()
        elif heights[i] - heights[i-1] == 1:
            heights[i] -= 1
    print("Yes")

if __name__ == '__main__':
    main()