def main():
    # Get the number of elements in the sequence
    num_elems = int(input())
    # Get the sequence
    seq = input().split()
    # Get the number of operations
    num_ops = int(input())
    # Get the operations
    ops = []
    for i in range(num_ops):
        ops.append(input().split())
    # For each operation, replace the elements in the sequence
    for i in range(num_ops):
        for j in range(num_elems):
            if seq[j] == ops[i][0]:
                seq[j] = ops[i][1]
    # Print the sum of the elements in the sequence
    print(sum(map(int, seq)))
