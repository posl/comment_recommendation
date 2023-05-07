def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]
    #N = 200000
    #S = [random.randint(1, 10**9) for _ in range(N)]
    #T = [random.randint(1, 10**9) for _ in range(N)]
    #print(N)
    #print(' '.join([str(x) for x in S]))
    #print(' '.join([str(x) for x in T]))
    #print()
    # min time to receive a gem
    min_time = [0] * N
    # next gem to receive
    next_gem = [0] * N
    # gem to receive
    gems_to_receive = [0] * N
    # gems to receive
    gems_to_receive_count = 0
    # gem to give
    gems_to_give = [0] * N
    # gems to give
    gems_to_give_count = 0
    # gem to give
    gem_to_give = 0
    # gems to give
    gems_to_give_count = 0
    # time
    t = 0
    # initial state
    for i in range(N):
        min_time[i] = T[i]
        next_gem[i] = i
        gems_to_receive[i] = i
        gems_to_receive_count += 1
    # main loop
    while True:
        #print('t', t)
        #print('gems_to_receive_count', gems_to_receive_count)
        #print('gems_to_give_count', gems_to_give_count)
        #print('gems_to_receive', gems_to_receive)
        #print('gems_to_give', gems_to_give)
        #print()
        # receive gems
        if gems_to_receive_count > 0:
            #print('gems_to_receive_count > 0')
            #print()
            #print('gems_to_receive_count', gems_to_receive_count)
            #print('gems_to_receive', gems_to_receive)
            #print()
            #print('gems_to_give_count', gems_to_give_count)
            #print('gems_to_give', gems_to_give)
            #print()
            #print('next_gem', next_gem)
            #print
