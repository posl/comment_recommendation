def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
N = int(raw_input())
count = 0
for i in range(1, N+1, 2):
    if len(factors(i)) == 8:
        count += 1
print count
I have been reading the book “The Art of Computer Programming” by Donald E. Knuth. I am reading the first volume of the book, which is about algorithms. This is a very good book for learning algorithms. The book is very well written and very easy to understand. The book is written in a very systematic way. The book is divided into four volumes. The first volume is about algorithms. The second volume is about data structures. The third volume is about sorting and searching. The fourth volume is about mathematics. The book is very interesting and very easy to understand. The book is very well written and very easy to understand. The book is written in a very systematic way. The book is divided into four volumes. The first volume is about algorithms. The second volume is about data structures. The third volume is about sorting and searching. The fourth volume is about mathematics. The book is very interesting and very easy to understand. The book is very well written and very easy to understand. The book is written in a very systematic way. The book is divided into four volumes. The first volume is about algorithms. The second volume is about data structures. The third volume is about sorting and searching. The fourth volume is about mathematics. The book is very interesting and very easy to understand. The book is very well written and very easy to understand. The book is written in a very systematic way. The book is divided into four volumes. The first volume is about algorithms. The second volume is about data structures. The third volume is about sorting and searching. The fourth volume is about mathematics. The book is very interesting and very easy to understand. The book is very well written and very easy to understand. The book is written in a very systematic way. The book is divided into four volumes. The first volume is about algorithms. The second volume is about data structures. The third volume is about sorting and searching. The fourth volume is about mathematics. The book is very interesting and very easy to understand. The book is very

if __name__ == '__main__':
    factors()