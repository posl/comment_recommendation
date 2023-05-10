def main():
    N = int(input())
    a = list(map(int, input().split()))
    med = []
    for i in range(N):
        for j in range(i, N):
            med.append(a[i:j+1])
    med2 = []
    for i in range(len(med)):
        med2.append(sorted(med[i])[int((len(med[i])-1)/2)])
    print(sorted(med2)[int((len(med2)-1)/2)])
