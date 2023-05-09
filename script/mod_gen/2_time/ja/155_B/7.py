def is_ok(num):
    if num % 2 == 0:
        if num % 3 == 0 or num % 5 == 0:
            return True
    else:
        return False
N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if is_ok(A[i]) == False:
        print('DENIED')
        exit()
print('APPROVED')

if __name__ == '__main__':
    is_ok()