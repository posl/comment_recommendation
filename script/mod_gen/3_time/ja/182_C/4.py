def main():
    N = input()
    N_list = list(N)
    N_list = [int(i) for i in N_list]
    N_list.sort(reverse=True)
    N_list = [str(i) for i in N_list]
    N = ''.join(N_list)
    N = int(N)
    if N % 3 == 0:
        print(0)
        return
    elif N % 3 == 1:
        if N_list.count('1') > 0:
            print(1)
            return
        elif N_list.count('4') > 0:
            print(1)
            return
        elif N_list.count('7') > 0:
            print(1)
            return
        elif N_list.count('2') > 1:
            print(2)
            return
        elif N_list.count('5') > 1:
            print(2)
            return
        elif N_list.count('8') > 1:
            print(2)
            return
        elif N_list.count('2') > 0 and N_list.count('5') > 0:
            print(2)
            return
        elif N_list.count('2') > 0 and N_list.count('8') > 0:
            print(2)
            return
        elif N_list.count('5') > 0 and N_list.count('8') > 0:
            print(2)
            return
        elif N_list.count('2') > 0 and N_list.count('5') > 0 and N_list.count('8') > 0:
            print(2)
            return
        elif N_list.count('3') > 0 and N_list.count('6') > 0:
            print(2)
            return
        elif N_list.count('3') > 0 and N_list.count('9') > 0:
            print(2)
            return
        elif N_list.count('6') > 0 and N_list.count('9') > 0:
            print(2)
            return
        elif N_list.count('3') > 0 and N_list.count('6') > 0 and N_list.count('9') > 0:
            print(2)
            return
        elif N_list.count('3') > 1:
            print(3)
            return
        elif N_list.count('6') >

if __name__ == '__main__':
    main()