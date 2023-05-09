def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]
    #compute
    C = [0]*4
    for s in S:
        if s == 'AC':
            C[0] += 1
        elif s == 'WA':
            C[1] += 1
        elif s == 'TLE':
            C[2] += 1
        elif s == 'RE':
            C[3] += 1
    #output
    print('AC x', C[0])
    print('WA x', C[1])
    print('TLE x', C[2])
    print('RE x', C[3])
