### The Unscrupulous Diner's Dilemma

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

When we are evenly-splitting the bill, assume that the selfish player
thinks that others are buying the cheap item, and so can reduce the 
cost of the $10 burger; after all, with 5 people splitting the cost, 
its only $2 averaged over everyone. 

Hence, the inequality we are interested in is:

    (cost[exp] + (n-1)*cost[cheap])/n - c > ue-uc

What this means is, if we assume everyone else gets the cheap meal, 
and thus our meal will not cost as much, then once this inequality 
is false, the extra utility of the meal becomes greater than the 
averaged-cost of the expensive meal, and so we buy it, because this
is a greater utility 'hit' for us we want. 

