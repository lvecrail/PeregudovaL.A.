A=1
B=3
C=1
D=5 
chisl=A*D-B*C
znam=B*D
a,b=chisl,znam 
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a 
print(f'{chisl // a}/{znam // a}')
