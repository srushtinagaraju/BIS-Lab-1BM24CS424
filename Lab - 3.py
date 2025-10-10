import random
from math import sqrt

c1, c2 = 1, 1


def fitness(x):
    return -x**2 + 5*x + 20


def init():
    n = int(input("Enter no. of particles: "))
    v = [0 for i in range(n)]
    x = list(map(float, input("Enter positions of particles:").split()))
    p = x.copy()
    fp = [fitness(xi) for xi in x]
    return n, v, fp, p, x


def find(n, fp, p):
    max_fitness = float('-inf')
    pos = -1
    for i in range(n):
        if fp[i] > max_fitness:
            max_fitness = fp[i]
            pos = i
    return pos


def update(n, v, fp, p, x, max_pos):
    r1, r2 = sqrt(random.random()), sqrt(random.random())

    for i in range(n):
        v[i] = v[i] + c1 * r1 * (p[i] - x[i]) + c2 * r2 * (p[max_pos] - x[i])
        x[i] = x[i] + v[i]

    for i in range(n):
        fp[i] = fitness(x[i])
        if fp[i] > fitness(p[i]):
            p[i] = x[i]


def print_state(v, fp, p, x):
    print(f'''
    {x}
    {p}
    {v}
    {fp}
    ''')


n, v, fp, p, x = init()
print_state(v, fp, p, x)
max_pos = find(n, fp, p)
gbest = p[max_pos]

while True:
    update(n, v, fp, p, x, max_pos)
    max_pos = find(n, fp, p)
    if fitness(gbest) == fitness(p[max_pos]):
        break
    print_state(v, fp, p, x)
    gbest = p[max_pos]

print(f"Global Best Solution: {gbest} with fitness: {fitness(gbest)}")



########OUTPUT#########
Enter no. of particles: 3
Enter positions of particles:1 2 3

    [1.0, 2.0, 3.0]
    [1.0, 2.0, 3.0]
    [0, 0, 0]
    [24.0, 26.0, 26.0]
    

    [1.1649251922563089, 2.0, 2.835074807743691]
    [1.1649251922563089, 2.0, 2.835074807743691]
    [0.16492519225630892, 0.0, -0.16492519225630892]
    [24.467575257728146, 26.0, 26.13772487321553]
    

    [2.8323105419777423, 2.7512300787325623, 2.6701496154873823]
    [2.8323105419777423, 2.7512300787325623, 2.6701496154873823]
    [1.6673853497214335, 0.7512300787325623, -0.16492519225630892]
    [26.13956970369046, 26.18688344754003, 26.221049108349497]
    

    [4.440795168486677, 3.473009795858875, 2.5052244232310734]
    [2.8323105419777423, 2.7512300787325623, 2.5052244232310734]
    [1.6084846265089345, 0.7217797171263128, -0.16492519225630892]
    [22.48331411397877, 25.30325193716267, 26.249972705401902]
    
Global Best Solution: 2.5052244232310734 with fitness: 26.249972705401902

