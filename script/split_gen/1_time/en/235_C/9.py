def process_queries(queries, numbers):
    #print(queries)
    #print(numbers)
    result = []
    for query in queries:
        #print(query)
        #print(numbers)
        #print(result)
        x = query[0]
        k = query[1]
        if k > len(numbers):
            result.append(-1)
        else:
            if x in numbers:
                if k <= numbers[x]:
                    result.append(numbers[x][k-1])
                else:
                    result.append(-1)
            else:
                result.append(-1)
    return result
