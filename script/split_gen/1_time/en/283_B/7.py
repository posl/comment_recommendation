def main():
    #Get the number of elements in the sequence
    n = int(input())
    #Get the sequence
    a = list(map(int, input().split()))
    #Get the number of queries
    q = int(input())
    #Process the queries
    for _ in range(q):
        #Get the query
        query = list(map(int, input().split()))
        #If the query is to set the value of an element in the sequence
        if query[0] == 1:
            #Get the index of the element to set
            k = query[1]
            #Get the value to set the element to
            x = query[2]
            #Set the value of the element
            a[k - 1] = x
        #If the query is to print the value of an element in the sequence
        else:
            #Get the index of the element to print
            k = query[1]
            #Print the value of the element
            print(a[k - 1])
