def get_triangles(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] > nums[k]:
                    count += 1
    return count

if __name__ == '__main__':
    get_triangles()