def is753(n):
    if "7" in str(n) and "5" in str(n) and "3" in str(n):
        return True
    else:
        return False
N = int(input())
count = 0
for i in range(1,N+1):
    if is753(i):
        count += 1
print(count)

if __name__ == '__main__':
    is753()