def calculate(A,B):
    result = B/A
    result = round(result,3)
    result = str(result)
    result = result+"000"
    return result[0:5]
A,B = input().split()
A = int(A)
B = int(B)
print(calculate(A,B))
