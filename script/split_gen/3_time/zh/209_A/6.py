def cal(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += 1
    return sum
a,b = input().split()
print(cal(int(a),int(b)))
