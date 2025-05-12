import random

x, y = 1.0, 1.0

delta = 0.1
n_iter =1000000
n_success= 0

for i in range(n_iter):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if abs(x + del_x) < 1.0 and abs(y + del_y)< 1.0:
        x, y = x + del_x, y + del_y
    if x**2 + y**2 < 1.0 : 
        n_success +=1

PI = 4.0 * n_success/ float(n_iter)

print(f"The computed value of Pi is {PI}")