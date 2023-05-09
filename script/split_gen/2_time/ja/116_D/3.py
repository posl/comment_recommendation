def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    sushi = sushi[:K]
    #print(sushi)
    t_set = set()
    t_list = []
    for t, d in sushi:
        if t not in t_set:
            t_set.add(t)
            t_list.append(t)
    #print(t_list)
    t_list.sort()
    #print(t_list)
    t_set = set(t_list)
    #print(t_set)
    #print(sushi)
    ans = 0
    for t, d in sushi:
        if t in t_set:
            ans += d
            t_set.remove(t)
    #print(ans)
    ans += len(t_list) * len(t_list)
    #print(ans)
    temp = ans
    #print(temp)
    for i in range(K-len(t_list)):
        #print(i)
        t, d = sushi[len(t_list)+i]
        #print(t, d)
        temp -= d
        #print(temp)
        temp -= len(t_list) * len(t_list)
        #print(temp)
        for j in range(len(t_list)-1, -1, -1):
            #print(j)
            t2, d2 = sushi[j]
            #print(t2, d2)
            if t2 != t:
                temp += d2
                #print(temp)
                temp += (len(t_list)-1) * (len(t_list)-1)
                #print(temp)
                temp -= (len(t_list)) * (len(t_list))
                #print(temp)
                if temp > ans:
                    ans = temp
                break
        else:
            break
    print(ans)
