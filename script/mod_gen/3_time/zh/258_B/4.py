def maxNum(N, nums):
    maxNum = 0
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1 or j == 0 or j == N-1:
                #up
                if i - 1 >= 0:
                    if nums[i-1][j] > nums[i][j]:
                        continue
                #down
                if i + 1 < N:
                    if nums[i+1][j] > nums[i][j]:
                        continue
                #left
                if j - 1 >= 0:
                    if nums[i][j-1] > nums[i][j]:
                        continue
                #right
                if j + 1 < N:
                    if nums[i][j+1] > nums[i][j]:
                        continue
                #up-left
                if i - 1 >= 0 and j - 1 >= 0:
                    if nums[i-1][j-1] > nums[i][j]:
                        continue
                #up-right
                if i - 1 >= 0 and j + 1 < N:
                    if nums[i-1][j+1] > nums[i][j]:
                        continue
                #down-left
                if i + 1 < N and j - 1 >= 0:
                    if nums[i+1][j-1] > nums[i][j]:
                        continue
                #down-right
                if i + 1 < N and j + 1 < N:
                    if nums[i+1][j+1] > nums[i][j]:
                        continue
                maxNum = max(maxNum, nums[i][j])
    return maxNum

if __name__ == '__main__':
    maxNum()