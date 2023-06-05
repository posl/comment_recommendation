def main():
    #import time
    #start = time.clock()
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))
    #end = time.clock()
    #print(end - start)
