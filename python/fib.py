
'''   0           when n = 0
	         1           when n = 1
      2pell(n-1) + pell(n-2) when n > 1
'''

def fibI(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    while n > 1:
         return 2pell(n-1) + pell(n-2)
         n -= 1
