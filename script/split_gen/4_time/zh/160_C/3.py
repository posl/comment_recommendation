def solve(k,n,an):
    # 1. 从第一个房子开始，依次访问，计算总距离
    # 2. 从第二个房子开始，依次访问，计算总距离
    # 3. 从第三个房子开始，依次访问，计算总距离
    # 4. 从第n个房子开始，依次访问，计算总距离
    # 5. 找出最小距离
    # 6. 输出最小距离
    min_dist = 10**6
    for i in range(n):
        dist = 0
        for j in range(n):
            dist += min(abs(an[(i+j)%n]-an[(i+j-1)%n]),k-abs(an[(i+j)%n]-an[(i+j-1)%n]))
        min_dist = min(min_dist,dist)
    print(min_dist)
