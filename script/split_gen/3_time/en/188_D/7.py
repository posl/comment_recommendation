def main():
    #N: number of services
    #C: price of Snuke Prime
    #a_i: start date of the i-th service
    #b_i: end date of the i-th service
    #c_i: price of the i-th service
    N, C = map(int, input().split())
    #service_list: list of lists
    #service_list[i] = [a_i, b_i, c_i]
    service_list = []
    for i in range(N):
        a_i, b_i, c_i = map(int, input().split())
        service_list.append([a_i, b_i, c_i])
    #sort service_list by a_i
    service_list.sort()
    #print(service_list)
    #service_list2: list of lists
    #service_list2[i] = [a_i, b_i, c_i, c_i_sum]
    #c_i_sum: sum of c_i from a_i to b_i
    service_list2 = []
    for i in range(N):
        a_i = service_list[i][0]
        b_i = service_list[i][1]
        c_i = service_list[i][2]
        c_i_sum = c_i
        for j in range(i+1, N):
            if service_list[j][0] == a_i:
                c_i_sum += service_list[j][2]
            else:
                break
        service_list2.append([a_i, b_i, c_i, c_i_sum])
    #print(service_list2)
    #service_list3: list of lists
    #service_list3[i] = [a_i, b_i, c_i, c_i_sum, c_i_sum_prime]
    #c_i_sum_prime: sum of c_i from a_i to b_i with Snuke Prime
    service_list3 = []
    for i in range(N):
        a_i = service_list2[i][0]
        b_i = service_list2[i][1]
        c_i = service_list2[i][2]
        c_i_sum = service_list2[i][3]
        c_i_sum_prime = c_i_sum
        for j in range(i+1, N):
            if service_list2[j][0] == a_i:
                if service_list2[j][1] < b_i:
                    c_i_sum_prime += service_list2
