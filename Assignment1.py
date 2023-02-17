import numpy as np
L=12 #Length of beam (meters, m)
w=10 #Load intensity (kilonewtons per meter, KN/m)

#Solving a
#Bending moment and shear force when x=0
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
m="When x=0, the bending moment is"
n="when x=0, the shear force is"
print()
print("(a.1)" + m + str(M) + "and", n + str(V))

#Bending moment and shear force when x=L
x=L
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
o="When x=L, the bending moment is"
p="when x=L, the shear force is"
print()
print("(a.2)" + o + str(M) + "and", p + str(V))

#Solving b
"""
When the bending moment M=0, we get the quadratic equation x**2-Lx + L**2/6 =0
"""
#From the expression,
a=1
b=-L
c=L**2/6
#From the almighty formula, the two roots are
discriminate=b**2-4*a*c
fir_root=(-b+np.sqrt(discriminate))/2*a
sec_root=(-b-np.sqrt(discriminate))/2*a
print()
print('(b)The points of contraflexure are {0} and {1}'.format(fir_root,sec_root))

#Solving c
"""
When the shear force is zero, x=L/2
"""

x=L/2
print()
print('(c)The point at which V=0 is {}'.format(x))

#Solving d
d=0
e=0.01
f=L+e
x=np.arange(d,f,e)
M=(w*(-6*x**2+6*L*x-L**2))/12
print()
print('(d)The bending moment at each step of the array is {0} using the initialized variable'.format(M))

#Solving e
V=w*(L/2-x)
print()
print('(e)The shear force for each step along the span is {}'.format(V))

#Solving f
"""
Let the absolute value of the bending moment array AM and the minimum value of AM be minAM
"""
#From the expression
AM= abs(M)
minAM= min(AM)

"""
When the bending moment is minAM, the get the equation x**2-Lx+(L**2/6)=(2*minAM)/w=0
"""
#From the expression above
a=1
b=-L
c=(L**2/6)+(2*minAM)/w

#Using the almighty formula to find the roots,
discriminant=b**2-4*a*c
thir_root=(-b+np.sqrt(discriminant))/2*a
four_root=(-b-np.sqrt(discriminant))/2*a
print()
print('(f)The point alongs along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(thir_root,four_root))

#Solving g
"""
Let the relative errors be re
"""
re1=((fir_root-thir_root)/fir_root*100)
re2=((four_root-sec_root)/four_root*100)
print()
print('(g)The relative errors between the estimated between points of contra-flexure are {0}% and {1}%'.format(re1,re2))

#Solving h
"""
Let the maximum bending moment be maxM and the minimum bending moment be minM
"""
#For maximum
maxM=max(M)
"""
When the bending moment is maxM, we get an expression x**2-Lx+(L**2/6)+(2*maxM)/w=0
                                                               
"""
a=1
b=-L
c=(L**2/6)+(2*maxM)/w

#Using the almighty formula, the two roots are
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a

print()
print('(h.1)The points at which the maximum bending moment occur are {0} and {1}'.format(root_1,root_2))

#For minimum
minM=min(M)
"""
When the bending moment is maxM, we get an expression x**2-Lx+(L**2/6)+(2*minM)/w=0

"""
a=1
b=-L
c=(L**2/6)+(2*minM)/w

#Using the almighty formula, the two roots are
discriminant=b**2-4*a*c
root_1=(-b-np.sqrt(discriminant))/2*a
root_2=(-b+np.sqrt(discriminant))/2*a

print()
print('(h.2)The points at which the minimum bending moment occur are {0} and {1}'.format(root_1,root_2))



