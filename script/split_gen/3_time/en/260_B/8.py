def main():
  # Read the input
  N, X, Y, Z = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  # Prepare the list of the examinees
  examinees = []
  for i in range(N):
    examinees.append((A[i], B[i], A[i]+B[i], i+1))
  # Sort the list of the examinees in the descending order by the total score
  examinees.sort(key=lambda x: x[2], reverse=True)
  # Admit the examinees with the highest total scores
  admitted = examinees[:Z]
  # Sort the list of the examinees in the descending order by the English score
  examinees.sort(key=lambda x: x[1], reverse=True)
  # Admit the examinees with the highest English scores
  admitted += examinees[:Y]
  # Sort the list of the examinees in the descending order by the math score
  examinees.sort(key=lambda x: x[0], reverse=True)
  # Admit the examinees with the highest math scores
  admitted += examinees[:X]
  # Sort the list of the examinees in the ascending order by the examinee number
  admitted.sort(key=lambda x: x[3])
  # Print the examinee numbers of the admitted examinees
  for examinee in admitted:
    print(examinee[3])
main()
I am sending you the codedump of Python3: How to sort a list of tuples in descending order by the first element, then by the second element, and so on? that you can see here: https://codedump.io/share/7s0nTlTn7VrG/1
