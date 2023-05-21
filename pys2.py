import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

n=1
R=0.08205
T=sy.symbols('T')
T1=300
#T2=265
V=sy.symbols('V')
Vx=sy.symbols('Vx')
Px=n*R*T/Vx
r=5/3

Va=10#Vx에대응
Vb=20
Vc=25
Vd=Va*Vc/Vb

Pa=n*R*T1/Va#Px에대응
Pb=n*R*T1/Vb
Pc=Pb*(Vb/Vc)**r
T2=Pc*Vc/n/R
#print(T2)
Pd=n*R*T2/Vd


V_ab=np.arange(Va,Vb+0.5,0.5)#V에대응
V_bc=np.arange(Vb,Vc+0.5,0.5)
V_cd=np.arange(Vd,Vc+0.5,0.5)
V_da=np.arange(Va,Vd+0.5,0.5)

def P(V,Px,Vx,r):#V:x좌표값,(Px,Vx):기준점,r:계수
  return Px*(Vx/V)**r
x=sy.symbols('x')
def inte(x,Px,Vx,r,a,b):
  return(float(sy.integrate(P(x,Px,Vx,r),(x,a,b))))#return으로

plt.plot(V_ab,P(V_ab,Pa,Va,1),c='b')
plt.plot(V_bc,P(V_bc,Pb,Vb,(5/3)),c='r')
plt.plot(V_cd,P(V_cd,Pc,Vc,1),c='g')
plt.plot(V_da,P(V_da,Pd,Vd,(5/3)),c='y')



S1=inte(x,Pa,Va,1,Va,Vb)
S2=inte(x,Pb,Vb,5/3,Vb,Vc)
S3=inte(x,Pd,Vd,5/3,Va,Vd)
S4=inte(x,Pc,Vc,1,Vd,Vc)



W=((S1+S2)-(S3+S4))
print('T1',T1,'T2',T2)
print('W',W)
print('e',(1-(T2/T1))*100,"%")



plt.show()

