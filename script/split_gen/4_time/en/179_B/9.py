def main():
    # Get input here
    N = int(input())
    doublets = []
    for _ in range(N):
        doublets.append(input().split())
    # Calculate result here
    count = 0
    for i in range(N):
        if doublets[i][0] == doublets[i][1]:
            count += 1
            if count == 3:
                break
        else:
            count = 0
    # Print result here
    if count == 3:
        print('Yes')
    else:
        print('No')
