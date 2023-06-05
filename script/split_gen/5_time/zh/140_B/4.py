def get_satisfaction(n, a, b, c):
    satisfaction = 0
    for i in range(n):
        satisfaction += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i]+1:
            satisfaction += c[a[i]-1]
    return satisfaction
