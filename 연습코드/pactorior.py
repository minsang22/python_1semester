n = int(input("n : "))
r = int(input("r : "))
n_fact=1
for i in range(1,n+1) :
    n_fact = n_fact*i
n_r_fact=1
for i in range(1,n-r+1) :
    n_r_fact=n_r_fact*i
print(int(n_fact/n_r_fact))
