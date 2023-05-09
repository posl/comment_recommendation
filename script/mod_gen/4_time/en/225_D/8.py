def main():
    #input
    N, Q = map(int, input().split())
    #The following 3 lists are used to store the information of the toy trains.
    #The i-th element of the list is the car number of the car connected to the rear of the i-th car.
    #If there is no car connected to the rear of the i-th car, the i-th element is 0.
    rear = [0] * N
    #The i-th element of the list is the car number of the car connected to the front of the i-th car.
    #If there is no car connected to the front of the i-th car, the i-th element is 0.
    front = [0] * N
    #The i-th element of the list is the car number of the car at the front of the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is i.
    front_of_component = [0] * N
    #The following 2 lists are used to store the information of the connected components.
    #The i-th element of the list is the number of cars in the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is the number of cars in the connected component.
    size_of_component = [0] * N
    #The i-th element of the list is the car number of the car at the front of the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is i.
    front_of_component = [0] * N
    #The following 2 lists are used to store the information of the connected components.
    #The i-th element of the list is the number of cars in the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is the number of cars in the connected component.
    size_of_component = [0] * N
    #The following 2 lists are used to store the information of the connected components.
    #The i-th element of the list is the number of cars in the connected component containing the i-th car.
    #If the i-th car is at the

if __name__ == '__main__':
    main()