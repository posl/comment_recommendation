def solve(n,x,ab):
    #先算出第一次全部通关的时间
    time = 0
    for i in range(n):
        time += ab[i][0] + ab[i][1]
    #print(time)
    #如果x大于第一次通关的时间，那么直接输出
    if x > time:
        return time
    #如果x小于第一次通关的时间，那么需要计算x次通关的时间
    else:
        #先计算出x次通关的最小时间
        time = 0
        for i in range(n):
            time += ab[i][0]
        #print(time)
        #如果x次通关的最小时间大于x，那么直接输出x
        if time > x:
            return x
        #如果x次通关的最小时间小于x，那么需要计算x次通关的时间
        else:
            #先计算出x次通关的最大时间
            time = 0
            for i in range(n):
                time += ab[i][0] + ab[i][1]
            #print(time)
            #如果x次通关的最大时间小于x，那么直接输出x次通关的最大时间
            if time < x:
                return time
            #如果x次通关的最大时间大于x，那么需要计算x次通关的时间
            else:
                #先计算出x次通关的最小时间
                time = 0
                for i in range(n):
                    time += ab[i][0]
                #print(time)
                #如果x次通关的最小时间等于x，那么直接输出x次通关的最小时间
                if time == x:
                    return time
                #如果x次通关的最小时间小于x，那么需要计算x次通关的时间
                else:
                    #先计算出x次通关的最大时间
                    time = 0
                    for i in range(n):
                        time += ab[i][0] + ab[i][1]
                    #print(time)
                    #如果x次
