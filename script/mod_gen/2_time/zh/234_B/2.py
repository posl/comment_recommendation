def get_max_distance(x_list, y_list):
    distance_list = []
    for i in range(len(x_list)):
        for j in range(i,len(x_list)):
            distance_list.append((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2)
    return max(distance_list)**(1/2)

if __name__ == '__main__':
    get_max_distance()