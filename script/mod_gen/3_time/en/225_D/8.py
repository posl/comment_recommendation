def main():
    N, Q = map(int, input().split())
    #N: number of cars
    #Q: number of queries
    
    #Initialize the list of cars
    #Each car is represented by a list of two elements: car number and the number of cars in the same connected component
    #The car number is the same as the index of the car in the list
    #The number of cars in the same connected component is 1 for each car initially
    cars = [[i, 1] for i in range(N)]
    
    #Initialize the list of queries
    queries = []
    for i in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
    
    #Initialize the list of connected components
    #Each connected component is represented by a list of car numbers
    #Initially, there are N connected components
    connected_components = [[i] for i in range(N)]
    
    #Process the queries
    for query in queries:
        #If the query is of the format 1 x y
        if query[0] == 1:
            x = query[1]
            y = query[2]
            
            #Get the car numbers of the cars in the connected component containing Car x
            x_cc = cars[x-1][0]
            x_cc_car_numbers = connected_components[x_cc]
            
            #Get the car numbers of the cars in the connected component containing Car y
            y_cc = cars[y-1][0]
            y_cc_car_numbers = connected_components[y_cc]
            
            #Get the number of cars in the connected component containing Car x
            x_cc_num_cars = len(x_cc_car_numbers)
            
            #Get the number of cars in the connected component containing Car y
            y_cc_num_cars = len(y_cc_car_numbers)
            
            #Update the car numbers of the cars in the connected component containing Car x
            for car_number in y_cc_car_numbers:
                cars[car_number][0] = x_cc
            
            #Update the number of cars in the connected component containing Car x
            cars[x-1][1] += y_cc_num_cars
            
            #Update the number of cars in the connected component containing Car y
            cars[y-1][1] = 1
            
            #Update the list of connected components
            x_cc_car_numbers.extend

if __name__ == '__main__':
    main()