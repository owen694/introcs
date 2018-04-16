def pell_iter(n):
    a = 1
    b = 2
    for i in range(3, n+1) :
        c = 2 * b + a
        a = b
        b = c
    return c
        

def pell_tree(n):
    if n == 0 or n == 1:
        return n
    i = 2 * pell_tree(n - 1) + pell_tree(n -2)
    return i 


def pelltester(p, n):
    for i in range(1, n + 1):
        print i, 'th term', p(i)
    print 'Done testing ', p

def main():
    n = int(raw_input('enter a positive integer: '))
    pelltester(penn_iter, n )
    pelltester(pell_tree, n)


