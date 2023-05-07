def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if A[i] != A[j]:
                count += 1
    print(count)
main()
I've been trying to solve this problem for a while now, and I keep getting the wrong answer. I've tried using a dictionary and a list, but I can't get it to work. I've also tried using a counter, but I can't get it to work either. I'm not sure what else to try, so I was wondering if anyone could help me out.
