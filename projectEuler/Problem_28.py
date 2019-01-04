'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

def sumSquare(n):
    #右上
    ru = (2*n+1)**2
    #左上
    lu = (2*n+1)**2 - (2*n)
    #左下
    ld = (2*n+1)**2 - (4*n)
    #右下
    rd = (2*n+1)**2 - (6*n)

    return [rd,ld,lu,ru]

fix = sum([sum(sumSquare(x)) for x in range(1,501)])+1
print(fix)
