def main():
    n = int(input())
    #n = 1000000007
    #n = 720
    num = 1
    #num_list = []
    while num <= n:
        if n % num == 0:
            #num_list.append(num)
            print(num)
        num += 1
    #print(num_list)
