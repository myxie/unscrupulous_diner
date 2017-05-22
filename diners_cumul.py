"""
Separating out the culumative modelling for the diner's dilemma.

In this file, we are showing that for a basic Diner's dilemma 
implementation, the decision to move is unchanged by the ratio of 
the cost difference and the utility difference
"""

import numpy as np
import matplotlib.pyplot as plt 

cost = []
cumul_cost = []
n_cost = [] 


ratios = [0.2,0.33,0.4,0.5]

ratio_costs = [[180,100,240,220],[80,50,90,80],[80,40,90,74],[30,10,50,40]]

ratio_results = []

players = [n for n in range(0,300)]

# e = 30
# c = 10
# ue = 50
# uc = 40 

for ratio_list in ratio_costs:
    cost = []
    cumul_cost = []
    n_cost = [] 

    e = ratio_list[0]
    c = ratio_list[1]
    ue = ratio_list[2]
    uc = ratio_list[3]

    print e-c
    print ue-uc
    number = len(players)
    #print players
    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]
        cumul_cost.append(sum(cost))
        if e-c > ue-uc:
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))

    fig = plt.figure()
    #ax1 = fig.add_subplot(111)
    util_c = uc-c
    util_e = ue-e
    plot_c = [util_c for x in range(len(players))]
    plot_e = [util_e for x in range(len(players))]

    ratio_results.append(cumul_cost)
    #ax1.plot(players,cumul_cost,label='Self')

    # ax2 = ax1.twinx()

    # ax2.plot(players, plot_c, label='Cheap utility')
    # ax2.plot(players, plot_e, label='Expensive utility(Self)')


    cost = []
    cumul_cost = []

    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]
        cumul_cost.append(sum(cost))
        if ((e+(number-1)*c)/number)-c > ue-uc:
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))
    e = (e+(number-1)*c)/number
    util_e = ue-e
    plot_e = [util_e for x in range(len(players))]
    ratio_results.append(cumul_cost)

    #ax1.plot(players,cumul_cost,label='Split')
# ax2.plot(players, plot_e, label='Expensive utility(Split)')
fig = plt.figure()
ax1 = fig.add_subplot(111)

count = 0
for result in ratio_results:
    print count
    if count %2 is 0:
        ax1.plot(players,result,color='b',label='Cheap: '+str(ratios[count/2]))
    else:
        ax1.plot(players,result,color='g',label='Cheap: '+str(ratios[(count-1)/2]))
    count = count + 1
plt.legend()
plt.show()
