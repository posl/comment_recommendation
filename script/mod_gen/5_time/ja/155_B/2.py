def is_evenly_divisible_by_3_or_5(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
        else:
            return False
    else:
        return False
N = int(input())
A = list(map(int, input().split()))
for a in A:
    if is_evenly_divisible_by_3_or_5(a) == False:
        print('DENIED')
        exit()
print('APPROVED')

if __name__ == '__main__':
    is_evenly_divisible_by_3_or_5()