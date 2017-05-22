"""
Visualise a basic Unscrupulous Diner's Dilemma
"""

import numpy as np
import matplotlib.pyplot as plt 


# Model the 'everyone pays for their own meal' 

players = [n for n in range(0,300)]

"""
Cost layouts for different ratios:
        e , c ; ue, uc
0.25 - [180,100;240,220]
0.33 - [80,50;90,80]
0.4 - [80,40;90,74]
0.5 - [30,10;50,40]
"""

# Costs
e = 30
c = 10
ue = 50
uc = 40 

#cost = [n, for n*50 in range(0,10)]

cost = [] 
cumul_cost = []
exp = []
cumul_exp = []

for n in players:
   exp = exp+ [e]
   cumul_exp.append(sum(exp))

n_cost = []
for number in range(10,300,10):
    players = [n for n in range(0,number)]
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
    final_cost=cumul_cost[number-1]
    n_cost.append(final_cost)
fig = plt.figure()
ax1 = fig.add_subplot(111)

xaxis = [x for x in range(10,300,10)]
ax1.plot(xaxis, n_cost,'ro', label='Cheap')
#
util_c = uc-c
util_e = ue-e
print util_c
print util_e
#exp = sum(expensive)
#cheap = sum(cheap)
ax2 = ax1.twinx()
plot_c = [util_c for x in range(len(players))]
plot_e = [util_e for x in range(len(players))]
ax1.set_xlabel('Number of players')
ax1.set_ylabel('Cumulative cost of dinner')
ax2.set_ylabel('Utility')

ax2_ticks = [n for n in range(0,50,10)]
print ax2_ticks
#ax2.set_yticks=ax2_ticks
#ax1.plot(players,cumul_cost,label='cumul_cost')
#ax2.plot(players, plot_c,label='Cheap utility')
#ax2.plot(players,plot_e,label='Expensive utility')
#plt.legend()
#fig.tight_layout()
#plt.show()
# Model the 'Split bill' scenario 
#(cost[exp] + (n-1)*cost[cheap])/n - c > ue-uc

"""
If everyone can see what 3 other people are doing
then everyone acting at once is acting based on 1/3 of n-1

So, if we know that 1 other person is eating the expensive option,
we can factor that into our decision.

We've chosen the expensive option; however, now the number of 
people choosing the expensive option has increased, according
to the 1 person who is eating the expensive option, we can 
factor that in to our calculations:

(e + ((number-1)/3)*e)/number + (number-(1-2((number-1)/3))*c)/number


"""

cost = []
cumul_cost = []
n_cost = [] 
util_diff = []
for number in range(10,300,10):
    players = [n for n in range(0,number)]
    #print players
    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]
        cumul_cost.append(sum(cost))
        if ((e+(number-1)*c)/number)-c > ue-uc:
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))

    final_cost=cumul_cost[number-1]
    n_cost.append(final_cost)
    
    e = (e+(number-1)*c)/float(number)
    util_c = uc-c
    util_e = ue-e

    util_diff.append(((uc-c)-(ue-e))*number)
    #plot_c = [util_c for x in range(number)]
    #plot_e = [util_e for x in range(number)]
    '''
    #ax1.plot(players, cumul_cost, label='cumul_cost: '+ str(number))
    ax2.plot(players, plot_c,'ro', label='Cheap utility: ' +str(number))
    ax2.plot(players, plot_e, 'go',label='Expensive utility: '+str(number))
    '''
xaxis = [x for x in range(10,300,10)]
ax1.plot(xaxis, n_cost,'bo', label='split bill')
ax2.plot(xaxis, util_diff,'c--', label='util_diff')
#plt.plot(players, cumul_cost)
#plt.plot(players, cumul_exp)


plt.legend()
plt.show()
#print num
#print (e+(num-1)*c)/float(num)-c 
print ue-uc





