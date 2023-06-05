def get_max_value(n,k,v):
    if n==1:
        return v[0]
    if k==0:
        return 0
    max_value = 0
    for i in range(0,n):
        for j in range(i+1,n+1):
            value = get_max_value(i,k-1,v[0:i]) + get_max_value(j-i,k-1,v[i:j]) + get_max_value(n-j,k-1,v[j:n])
            if value > max_value:
                max_value = value
    return max_value
