def main():
    #read input
    s = input()
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(input().split())
    #process
    #operations:
    #1: reverse
    #2: add to beginning
    #3: add to end
    #4: do nothing
    #initially, do nothing
    operation = 4
    #initially, empty string
    result = ""
    #for each query
    for query in queries:
        #if operation is 1 or 2
        if operation == 1 or operation == 2:
            #if query is 1
            if query[0] == '1':
                #reverse
                operation = 3 - operation
            #if query is 2
            else:
                #if query is 1
                if query[1] == '1':
                    #add to beginning
                    result += query[2]
                #if query is 2
                else:
                    #add to end
                    result = query[2] + result
        #if operation is 3 or 4
        else:
            #if query is 1
            if query[0] == '1':
                #reverse
                operation = 7 - operation
            #if query is 2
            else:
                #if query is 1
                if query[1] == '1':
                    #add to beginning
                    result = query[2] + result
                #if query is 2
                else:
                    #add to end
                    result += query[2]
    #if operation is 1 or 2
    if operation == 1 or operation == 2:
        #reverse
        result = result[::-1]
    #if operation is 3 or 4
    else:
        #do nothing
        pass
    #output
    print(result)
main()

if __name__ == '__main__':
    main()