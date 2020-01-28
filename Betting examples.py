#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# ### Game:

# #### you win if number is between  51 and 99

# #### you lose if number is between 1 and 50 OR 100

# In[4]:


# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        print(roll,'- roll was 100, you lose. What are the odds?! Play again!')
        return False
    elif roll <= 50:
        print(roll,'- roll was 1-50, you lose.')
        return False
    elif 100 > roll >= 50:
        print(roll,'- roll was 51-99, you win!')
        return True


# In[5]:


rollDice()


# #### 1 person plays the game 100 times and then stops

# In[6]:


'''
Simple bettor, betting the same amount each time.
'''
# funds is amount of money we start off with
# initial wager is how much money we put in at each bet
# wager count is how often we bet

# we bet the same amount each time
def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    currentWager = 0

    while currentWager < wager_count:
        if rollDice():
            value += wager # if true (i.e. if we won) add money we put in
        else:
            value -= wager # if false (i.e. we lost) deduct money we put in

        currentWager += 1
    
    if value < 0:
        value = 'bankrupt'
        
    print('Funds:', value)



simple_bettor(10000,100,100)


# #### Multiple people play the game 100 times each

# In[7]:


# small change to just get final funds output
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True


# In[8]:


# Reminder on meaning: each player starts with 10000$, bets 50$ per round, and plays 100 rounds
x = 0

while x < 100:
    simple_bettor(10000,100,100) # change times we play from 10 to 1000 to demonstrate law of big numbers
    x += 1


# In[9]:


import matplotlib
import matplotlib.pyplot as plt


# #### Adding a few lines do our bettor to be able to plot it (idea remains the same as before)

# In[10]:


def simple_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager

    # number of times you betted on x axis
    wX = []

    # value of your money on y axis
    vY = []

    # change to 1, to avoid confusion so we start @ wager 1
    # instead of wager 0 and end at 100. 
    currentWager = 1

    #           change this to, less or equal.
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            # append so that each round of betting gets added to the plot
            wX.append(currentWager)
            vY.append(value)
            
        else:
            value -= wager
            # append append so that each round of betting gets added to the plot
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1
        

    plt.plot(wX,vY)
    


x = 0

# start this off @ 1, then add, and increase 10 to 100, then 1000
while x < 50:
    simple_bettor(10000,100,10000)
    x += 1


plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()


# #### New strategy: double up on losses

# In[11]:


import time


# #### 1 Player

# In[12]:


def doubler_bettor(funds,initial_wager,wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1

    # since we'll be betting based on previous bet outcome #
    previousWager = 'win'

    # since we'll be doubling #
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            print('we won the last wager, yay!')
            if rollDice():
                value += wager
                print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager  
                previousWager = 'loss'
                print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print('went broke after',currentWager,'bets')
                    break
        elif previousWager == 'loss':
            print('we lost the last one, so we will be super smart & double up!')
            if rollDice():
                wager = previousWagerAmount * 2
                print('we won',wager)
                value += wager
                print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                print('we lost',wager)
                value -= wager
                if value < 0:
                    print('went broke after',currentWager,'bets')
                    break
                print(value)
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    print('went broke after',currentWager,'bets')
                    break

        currentWager += 1

    print(value)
    plt.plot(wX,vY)

    
            
            
doubler_bettor(10000,100,1000)
plt.show()
# time.sleep(555)


# #### Multiple players (base case = 1000 people)

# In[13]:


def doubler_bettor(funds,initial_wager,wager_count):
    global broke_count
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1

    # since we'll be betting based on previous bet outcome #
    previousWager = 'win'

    # since we'll be doubling #
    previousWagerAmount = initial_wager

    '''
    immediately with these comments, and our previous discussion of how previous outcomes
    do not affect future outcome possibilities, you should realize that this betting method
    offers nothing more than a quicker realization of losses or gains.

    Another way to visualize this quicker realization is actually an increase in risk.
    This bettor will experience extremely unpredictable volatility most likely. 
    '''

    while currentWager <= wager_count:
        if previousWager == 'win':
            ##print 'we won the last wager, yay!'
            if rollDice():
                value += wager
                ##print value
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                ##print value
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    ##print 'went broke after',currentWager,'bets'
                    broke_count += 1
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            ##print 'we lost the last one, so we will be super smart & double up!'
            if rollDice():
                wager = previousWagerAmount * 2
                ##print 'we won',wager
                value += wager
                ##print value
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                ##print 'we lost',wager
                value -= wager
                ##print value
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    ##print 'went broke after',currentWager,'bets'
                    currentWager += 10000000000000000
                    broke_count += 1

        currentWager += 1


    plt.plot(wX,vY)

    

xx = 0
broke_count = 0

while xx < 1000:# change here amount of people taking part 
    doubler_bettor(10000,100,100)
    xx+=1

print('death rate:',(broke_count/float(xx)) * 100)
print('survival rate:',100 - ((broke_count/float(xx)) * 100))
plt.axhline(10000, color = 'r')
plt.show()


# ### Inputs

# In[14]:


# samples
sampleSize = 1000
# for bettors
startingFunds = 10000
wagerSize = 100
wagerCount = 1000


# #### Comparison

# In[15]:


def doubler_bettor(funds,initial_wager,wager_count,color):

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    currentWager += 10000000000000000
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2

                # this makes it so we just bet all that is left. 
                if (value - wager) < 0:
                    wager = value
                    
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                # this makes it so we just bet all that is left. 
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)


                # change to equals zero!
                if value <= 0:
                    currentWager += 10000000000000000

        currentWager += 1
    ########################### this guy edits color #
    plt.plot(wX,vY,color)


'''
Simple bettor, betting the same amount each time.
'''
#####                                           color#
def simple_bettor(funds,initial_wager,wager_count,color):


    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            ### change this part, not lessthan or equal zero, it is zero
            if value <= 0:
                currentWager += 10000000000000000
        currentWager += 1

    # this guy goes green #
    plt.plot(wX,vY,color)

    
x = 0

while x < sampleSize:             
    simple_bettor(startingFunds,wagerSize,wagerCount,'c')
    #simple_bettor(startingFunds,wagerSize*2,wagerCount,'c')
    doubler_bettor(startingFunds,wagerSize,wagerCount,'k')
    x+=1

plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()

