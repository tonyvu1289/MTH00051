import math
import copy
def mul_scalar_vector(alpha,v):
    return [x*alpha for x in v]

def add_vector(u,v):
    return [x+y for (x,y) in zip(u,v)]

def row_switch(A, i, j):
    A[i],A[j] = A[j],A[i]

def row_mul(A,i,k):
    A[i] = mul_scalar_vector(k,A[i])
    return A
def row_add(A,i,j,alpha):
    '''di = di + alpha.dj'''
    A[i] = add_vector(A[i],mul_scalar_vector(alpha,A[j]))
    return A

def is_zero(x):
    return math.isclose(x,0,abs_tol=1e-09)

def Gauss_elimination(A):
    R = copy.deepcopy(A)
    m,n = len(R), len(R[0]) 
    row  = col = 0
    # m is number of row, n is number of collumn
    #         n
    #       __^__  
    #      /     \
    #    |  *****
    #    |  *****
    #  m{   *****
    #    |  *****
    while row<m:
        while col<n and all(is_zero(R[i][col])for i in range(col,m)):
            
