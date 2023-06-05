def main():
    #读入数据
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    #print(n, k, p, c)
    #print(len(p), len(c))
    
    #定义最大分数
    max_score = -10**9 - 1
    
    #遍历所有可能的起点
    for i in range(n):
        #print('i =', i)
        #定义当前分数
        current_score = 0
        #定义当前位置
        current_position = i
        #定义当前步数
        current_step = 0
        #定义当前最大分数
        current_max_score = -10**9 - 1
        #定义当前循环的步数
        current_loop_step = 0
        #定义当前循环的最大分数
        current_loop_max_score = -10**9 - 1
        
        #如果k大于n，则可以循环k//n次，再加上k%n次
        if k >= n:
            #print('k >= n')
            #print('k // n =', k // n)
            #print('k % n =', k % n)
            #遍历k//n次
            for j in range(k // n):
                #print('j =', j)
                #print('current_step =', current_step)
                #print('current_position =', current_position)
                #print('current_score =', current_score)
                #print('current_max_score =', current_max_score)
                
                #如果当前位置和当前步数的最大分数大于当前循环的最大分数，则更新当前循环的最大分数
                if c[p[current_position] - 1] + current_score > current_loop_max_score:
                    current_loop_max_score = c[p[current_position] - 1] + current_score
                
                #更新当前位置
                current_position = p[current_position] - 1
                #更新当前步数
                current_step += 1
                #更新当前分数
                current_score += c[current_position]
                
                #如果当前位置和当前步数的最大分数大于当前最
