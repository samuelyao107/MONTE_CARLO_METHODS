import random

n_iter = 100000
n_success=0

for iter in range(n_iter):
    x,y = random.uniform(-1.0,1.0), random.uniform(-1.0,1.0)
    if x**2 + y**2 < 1.0:
        n_success +=1

PI = 4.0 * n_success/float(n_iter)

print(f'The computed value of pi is {PI}')