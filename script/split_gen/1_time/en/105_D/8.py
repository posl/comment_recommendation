def countSubarrays(arr, n, m): 
    mod = [0] * m 
  
    cumSum = 0
    for i in range(n): 
        cumSum = (cumSum + arr[i]) % m 
        mod[cumSum] += 1
  
    result = 0 
    for i in range(m): 
        if (mod[i] > 1): 
            result += (mod[i] * (mod[i] - 1)) // 2
  
    result += mod[0] 
    return result 
  
n, m = map(int, input().split()) 
arr = list(map(int, input().split())) 
  
print(countSubarrays(arr, n, m))
