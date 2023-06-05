def main():
    n = int(input())
    n_list = [x for x in range(2,n+1)]
    for i in range(2,n+1):
        for j in range(2,n+1):
            if i**j in n_list:
                n_list.remove(i**j)
    print(len(n_list))

if __name__ == '__main__':
    main()