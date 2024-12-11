list_a = range(1,10,2)
x = [ [a**2, a**3] for a in list_a]
print(x)

def kuadrat(x):
    return x*x
a = 10
k = kuadrat(a)
print('nilai kuadrat dari {} adalah {}'.format(a, k))

a = 5.5
print(a, "is of type", type(a))


