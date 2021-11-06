import math
import copy
def mul_scalar_vector(alpha,v):
    return [x*alpha for x in v]

def add_vector(u,v):
    return [x+y for (x,y) in zip(u,v)]

def row_switch(R, i, j):
    R[i],R[j] = R[j],R[i]

def row_mul(R,i,k):
    R[i] = mul_scalar_vector(k,R[i])
    return R
def row_add(R,i,j,alpha):
    '''di = di + alpha.dj'''
    R[i] = add_vector(R[i],mul_scalar_vector(alpha,R[j]))
    return R

def is_zero(x):
    return math.isclose(x,0,abs_tol=1e-09)

def GaussJordan_elimination(A):
    R=copy.deepcopy(A)
    m, n = len(R), len(R[0])
    row=col=0
    while row<m:
        while col<n and all(is_zero(R[i][col]) for i in range(row,m)):
            col +=1
        if col==n:
            break
        #chọn dòng đầu tiên có số hạng khác 0
        pivot_row=row+ [is_zero(R[i][col]) for i in range(row,m)].index(False)
        row_switch(R,row,pivot_row)
        row_mul(R,row,1/R[row][col])
        for i in range(m):
            if(i==row):
                continue
            row_add(R,i,row,-R[i][col])

        row += 1
    return R

def matrannghichdao(A):
    #lấy thông số
    m, n = len(A), len(A[0])
    if(m != n):
        return 0

    I = [ [0]*n for _ in range(n) ]
    for i in range (n):
        I[i][i] = 1
    R = [a+b for (a,b) in zip(A,I)]
    R = GaussJordan_elimination(R)
    for i in range(n):
        if(R[i][:n])!= I[i]:
            return 0
    return [line[n:]for line in R]
            

print('Nhap so dong: m = ')
m=int(input())
print('Nhap so cot: n = ')
n=int(input())
A = [ [0]*n for _ in range(m) ]
for i in range(m):
    for j in range(n):
        print('A[{}][{}]='.format(i,j))
        A[i][j] = int(input())
        print('\n')
B = matrannghichdao(A)
if(B):
    print(B)
else:
    print('Ma tran khong kha nghich')