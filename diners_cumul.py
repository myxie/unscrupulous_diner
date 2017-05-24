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


ratios = [0.25,0.33,0.4,0.5,0.75]

ratio_costs = [[180,100,240,220],[80,50,90,80],[110,70,120,104],[30,10,50,40],[130,90,150,120]]

ratio_results = []

players = [n for n in range(0,300)]

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
    ratio_results.append(cumul_cost)


#Model guilt

    cost = []
    cumul_cost = []

    for n in players:
        # 'Choose' Expensive option, as it is preferred 
        cost = cost + [e]

        cumul_cost.append(sum(cost))
        # if ((e+(number-1)*c)/number)-c > ue-uc:
        if (3*e + c)/4 - c > ue-uc:
            print ratio_list
            cumul_cost.remove(sum(cost))
            cost.remove(e)
            cost = cost+[c]
            cumul_cost.append(sum(cost))
    e = (e+(number-1)*c)/number
    ratio_results.append(cumul_cost)

fig = plt.figure()

count = 0
for result in ratio_results:
    print count
    if count %2 is 0:
        cheap, = plt.plot(players,result,color='b',label='Cheap')
        plt.text(players[-1], result[-1], str(ratios[(count/2)]))
    else:
        expensive, =plt.plot(players,result,'r--',label='Expensive')
        plt.text(players[-1], result[-1], str(ratios[(count/2)]))

    count = count + 1

plt.title("Cumulative cost of Expensive and Cheap meals\n for different Joy:Cost ratios for n=300\n with 'guilt'")
plt.xlabel('Number of players')
plt.ylabel('Cumulative Cost')
plt.legend(handles=[cheap, expensive])
plt.show()
