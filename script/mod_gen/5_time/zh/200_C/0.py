def count_pairs(arr):
    # Write your code here
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i]-arr[j])%200 == 0:
                count += 1
    return count

if __name__ == '__main__':
    count_pairs()