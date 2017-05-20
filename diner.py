"""
Visualise a basic Unscrupulous Diner's Dilemma
"""

import numpy as np
import matplotlib.pyplot as plt 


"""
N - number of players

c - cost of cheap meal
e - cost of expensive meal 

uc - utility of cheap meal
ue - utility of expensive meal

e > c 
e - c > ue - uc (Cost outweighs relative utility)

For splitting the bill:
Cost[exp] - Cost[cheap] < Util[Exp]-Util[cheap]

How do we model this? 

Example; salad is $5, burger and chips $10

We prefer the burger, but not enough to want to pay for it

So we want the cost[exp] - cost[cheap] to be <= Util[exp]-util[cheap]

When we are evenly-splitting the bill
"""


# Model the 'everyone pays for their own meal' 

players = [n, for n in range(0,300)]

# Costs
e = 30
c = 10
ue = 50
uc = 40

expensive = []
cheap = []

for n in players:
   # 'Choose' Expensive option, as it is preferred 
   expensive.append(n)
   if e-c > ue-uc
