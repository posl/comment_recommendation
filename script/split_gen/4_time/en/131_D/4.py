def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append([B, A])
    jobs.sort()
    time = 0
    for B, A in jobs:
        time += A
        if time > B:
            print("No")
            return
    print("Yes")
    return
main()
This is my first post on my blog. I am going to write about the problems that I have solved on AtCoder.
I am going to start with the problems from the ABC 131 contest. I have solved 5 problems from this contest. I will write about the problems that I have solved.
I have solved the C and D problems. The C problem was easy. The D problem was a bit difficult. I have solved this problem using the greedy algorithm. I did not know about the greedy algorithm before this contest. I have learnt about this algorithm from this problem. I have solved this problem in Python. I will post the code for this problem in my next post.
This is my first post on my blog. I am going to write about the problems that I have solved on AtCoder. I am going to start with the problems from the ABC 131 contest. I have solved 5 problems from this contest. I will write about the problems that I have solved. I have solved the C and D problems. The C problem was easy. The D problem was a bit difficult. I have solved this problem using the greedy algorithm. I did not know about the greedy algorithm before this contest. I have learnt about this algorithm from this problem. I have solved this problem in Python. I will post the code for this problem in my next post.
