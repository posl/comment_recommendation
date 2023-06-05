def sum_of_arithmetic_sequence(a1,an,n):
    return (a1+an)*n/2
n = int(input())
sum = 0
for i in range(n):
    ai, bi = map(int, input().split())
    sum += sum_of_arithmetic_sequence(ai,bi,bi-ai+1)
print(int(sum))

if __name__ == '__main__':
    sum_of_arithmetic_sequence()