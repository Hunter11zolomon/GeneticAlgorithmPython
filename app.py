import numpy as np 
import matplotlib.pyplot as plt
from ypstruct import structure
import ga

# Cost function
def sphere(x):
    return sum(x**2)

def costfunction(x):
    return x+1

# Problem Definition
problem = structure()
problem.costfunc = sphere   #Give your cost function here; an example of such is given in the line below
#problem.costfunc = costfunction

problem.nvar = 5                            #Number of variables for the minimization
problem.varmin = [-10, -2, 3, -4, -5]       #Lower bound for variable; Should be an array with length nvar if you want to use different bounds for each variable
problem.varmax = [10, 10, 10, 4, 5]       #Upper bound for variable; Should be an array with length nvar if you want to use different bounds for each variable


# GA Parameters
params = structure()
params.maxit = 10000      #Max no. of iterations
params.npop = 50        #Initial population size
params.beta = 1         #Selection pressure
params.pc = 1           #Number of offsprings after crossover as a ratio. 1 means no of initial population = no. of offsprings
params.gamma = 0.1      #Parameter to explore search phase ( 0->0.5 )
params.mu = 0.1         #Mutation rate (How much of the position changes)
params.sigma = 0.1      #Mutation stepsize



# Run GA
out = ga.run(problem, params)

# Results
#plt.plot(out.bestcost)
plt.semilogy(out.bestcost)
plt.xlim(0,params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm')  #Graph title here
plt.grid(True)
plt.show()