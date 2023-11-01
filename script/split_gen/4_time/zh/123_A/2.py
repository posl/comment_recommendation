def main():
    antennas = []
    for i in range(5):
        antennas.append(int(input()))
    k = int(input())
    for i in range(4):
        for j in range(i+1,5):
            if antennas[j] - antennas[i] > k:
                print
