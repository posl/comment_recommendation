def solve():
    S = input()
    Q = int(input())
    query = [list(map(int, input().split())) for i in range(Q)]
    for t,i in query:
        if t == 0:
            print(S[i-1])
            continue
        if S == "ABC":
            if i%3 == 1:
                print("A")
            elif i%3 == 2:
                print("B")
            else:
                print("C")
        elif S == "ACB":
            if i%3 == 1:
                print("A")
            elif i%3 == 2:
                print("C")
            else:
                print("B")
        elif S == "BAC":
            if i%3 == 1:
                print("B")
            elif i%3 == 2:
                print("A")
            else:
                print("C")
        elif S == "BCA":
            if i%3 == 1:
                print("B")
            elif i%3 == 2:
                print("C")
            else:
                print("A")
        elif S == "CAB":
            if i%3 == 1:
                print("C")
            elif i%3 == 2:
                print("A")
            else:
                print("B")
        elif S == "CBA":
            if i%3 == 1:
                print("C")
            elif i%3 == 2:
                print("B")
            else:
                print("A")
solve()
I was able to solve this problem by myself, but I don't think this is the best solution.
I also tried to solve the problem using the concept of the recurrence relation, but I couldn't solve it.
I would like to know if there is a better solution.
Thank you for reading.
I'm not sure if this is the best solution, but I think it's a good solution.
I think it's a good solution because it's easy to understand and it's easy to implement.
I think it's a good solution because it's easy to understand and it's easy to implement.
I think it's a good solution because it's easy to understand and it's easy to implement.
I think it's a good solution because it's easy to understand and it's easy to implement.
I think it's a good solution because it's easy to understand and it's easy to implement.
