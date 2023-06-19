def getPermutation(n,k):
    if n==1:
        return '1'
    nums = [i for i in range(1,n+1)]
    res = ''
    while n>0:
        if k==1:
            res += ''.join(str(i) for i in nums)
            break
        else:
            if k==factorial(n):
                nums.reverse()
                res += ''.join(str(i) for i in nums)
                break
            else:
                if k%factorial(n-1)==0:
                    index = k/factorial(n-1)
                else:
                    index = k/factorial(n-1)+1
                res += str(nums[index-1])
                nums.remove(nums[index-1])
                k = k%factorial(n-1)
                n -= 1
    return res
