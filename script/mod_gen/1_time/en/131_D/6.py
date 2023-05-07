def main():
    N = int(input())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs = sorted(jobs, key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print('No')
            return
    print('Yes')
main()
I have a list of tuples and I want to sort them by the second element of the tuple. I have tried the following code:
sorted(my_list, key=lambda x: x[1])
But it returns the following error:
TypeError: '<' not supported between instances of 'str' and 'int'
I am using Python 3.7.3.
I have a list of tuples and I want to sort them by the second element of the tuple. I have tried the following code:
sorted(my_list, key=lambda x: x[1])
But it returns the following error:
TypeError: '<' not supported between instances of 'str' and 'int'
I am using Python 3.7.3.
I want to sort a list of tuples by the second element of the tuple. I have tried the following code:
sorted(my_list, key=lambda x: x[1])
But it returns the following error:
TypeError: '<' not supported between instances of 'str' and 'int'
I am using Python 3.7.3.
I have a list of tuples and I want to sort them by the second element of the tuple. I have tried the following code:
sorted(my_list, key=lambda x: x[1])
But it returns the following error:
TypeError: '<' not supported between instances of 'str' and 'int'
I am using Python 3.7.3.
I have a list of tuples and I want to sort them by the second element of the tuple. I have tried the following code:
sorted(my_list, key=lambda x: x[1])
But it returns the following error:
TypeError: '<' not supported between instances of 'str' and 'int'
I am using Python 3.7.3.
I have a list of tuples and I want to sort them by the second element of the tuple. I have tried the following code:
sorted(my_list, key=lambda x: x[1])
But it returns the following error:
TypeError: '<

if __name__ == '__main__':
    main()