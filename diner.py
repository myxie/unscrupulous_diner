"""
Visualise a basic Unscrupulous Diner's Dilemma
"""

import numpy as np
import matplotlib.pyplot as plt 




e = 30
c = 10
ue = 50
uc = 40 

max_pop = 1000
# Model the 'everyone pays for their own meal' 

cost = [] 
cumul_cost = []
exp = []

n_cost = []
for population in range(10,max_pop+1,10):
    players = [n for n in range(0,population)]
    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]
        cumul_cost.append(sum(cost))
        if e-c > ue-uc:
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))
            #print cost
    final_cost=cumul_cost[population-1]
    n_cost.append(final_cost)
fig = plt.figure()
ax1 = fig.add_subplot(111)

xaxis = [x for x in range(10,max_pop+1,10)]
ax1.plot(xaxis, n_cost,'y',label='Individual')

#Setup axes
ax1.set_xlabel('Population of players')
ax1.set_ylabel('Cumulative cost of dinner')
ax2 = ax1.twinx()
ax2.set_ylabel('Utility')



#Model Shared Split Bill

cost = []
cumul_cost = []
n_cost = [] 
util_diff = []
for population in range(10,max_pop+1,10):
    players = [n for n in range(0,population)]
    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]
        cumul_cost.append(sum(cost))
        if ((e+(population-1)*c)/population)-c > ue-uc:
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))

    final_cost=cumul_cost[population-1]
    n_cost.append(final_cost)
    
    e = (e+(population-1)*c)/float(population)
    util_c = uc-c
    util_e = ue-e

    util_diff.append(((uc-c)-(ue-e))/population)


ax1.plot(xaxis, n_cost,'g', label='Shared')
ax2.plot(xaxis, util_diff,'c--', label='Utility Difference')

"""
Model 'Guilt' population
"""
cost = []
cumul_cost = []
n_cost = [] 
util_diff = []
for population in range(10,max_pop+1,10):
    players = [n for n in range(0,population)]
    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]
        cumul_cost.append(sum(cost))
        if (3*e + c)/4 - c > ue-uc:
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))

    final_cost=cumul_cost[population-1]
    n_cost.append(final_cost)
    
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()

# ax1.plot(xaxis, n_cost,'b.', label='Guilt')
plt.title("Cumulative cost of dinner with respect to utility\n difference as a proportion of population size.")
# ax1.legend(loc=4)
# ax2.legend(loc=0)
ax1.legend(h1+h2, l1+l2, loc=4)

plt.show()





