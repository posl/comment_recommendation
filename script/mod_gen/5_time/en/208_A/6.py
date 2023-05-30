def check_sum(a,b):
    for i in range(1,7):
        for j in range(1,7):
            if i+j == b:
                return 'Yes'
    return 'No'
a,b = map(int,input().split())
print(check_sum(a,b))
