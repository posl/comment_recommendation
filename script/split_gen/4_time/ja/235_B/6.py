def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    
    count = 0
    for i in range(1, n):
        if h_list[i-1] < h_list[i]:
            count = 0
        else:
            count += 1
        if count >= 2:
            print("No")
            exit()
    print("Yes")
