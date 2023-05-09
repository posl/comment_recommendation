def permutation(arr, num):
    if len(arr) == 1:
        return arr
    if num == 1:
        return arr
    else:
        n = len(arr)
        ans = []
        for i in range(n):
            for j in permutation(arr[:i] + arr[i+1:], num-1):
                ans.append(arr[i] + j)
        return ans

if __name__ == '__main__':
    permutation()