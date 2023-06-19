def main():
    N, M = map(int, input().split())
    k = []
    s = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        s.append(list(map(int, input().split())))
    p = list(map(int, input().split()))
    #print(N, M)
    #print(k)
    #print(s)
    #print(p)
    #灯泡i与k_i个开关相连：开关s_{i1}，s_{i2}，...，和s_{ik_i}。当这些开关中 "开 "的开关数与p_i的模数一致时，它就被点亮。
    #有多少种开关的 "开 "和 "关 "状态的组合可以点亮所有的灯泡？
    #建立一个N*M的二维数组，遍历每个开关，对于开关的每个开关，对于每个灯泡，如果灯泡与当前开关相连，则对应的二维数组的值+1
    #然后遍历二维数组，如果二维数组的值与p_i的模数一致，则灯泡i就是亮的，否则就是灭的
    #遍历所有的状态，如果所有的灯泡都是亮的，则计数器+1
    #输出计数器
    count = 0
    for i in range(2**N):
        #print(i)
        #i = 0
        #print(bin(i))
        #print(bin(i)[2:])
        #print(bin(i)[2:].zfill(N))
        #print(list(bin(i)[2:].zfill(N)))
        #print(list(map(int, bin(i)[2:].zfill(N))))
        #print(list(map(int, bin(i)[2:].zfill(N))[::-1]))
        #print(list(map(int, bin(i)[2:].zfill(N))[::-1][:N]))
        #print(list(map(int, bin(i)[2:].zfill(N))[::-1][:N][::-1]))
        #print(list(map(int, bin(i)[2:].zfill(N))[::-1][:

if __name__ == '__main__':
    main()