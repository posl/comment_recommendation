def count_different_sequences():
    N = int(input())
    sequences = []
    for i in range(N):
        sequences.append(input().split()[1:])
    #print(sequences)
    #print(len(sequences))
    sequences.sort()
    #print(sequences)
    #print(len(sequences))
    count = 1
    for i in range(1, N):
        if sequences[i] != sequences[i-1]:
            count += 1
    print(count)

if __name__ == '__main__':
    count_different_sequences()