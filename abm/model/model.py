# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:41:20 2022

@author: FMP
"""
import random
from abm.general import agentframework
import matplotlib
import matplotlib.pyplot
import csv
import matplotlib.animation
import statistics
#import importlib

#Greet the user
print("Let's introduce our parametres fot this model!")

'''Input from user, ask for number of agents, number of iteration and neighbourhood. 
If input is not an interger, it will print a message of error and ask again'''

while True:
    try:
        num_of_agents = int(input("Please insert number of agents: "))
        break
    except ValueError:
        print('A number is requested. Try again. For example, write 10')
        
while True:
    try:
        num_of_iterations = int(input("Please insert number of max iterations"+
                                      " to run in this model: "))
        break
    except ValueError:
        print('A number is requested. Try again. For example, write 100')
        
while True:
    try:
        neighbourhood = int(input("Please insert neighbourhood: "))
        break
    except ValueError:
        print('A number is requested. Try again. For example, write 20')        

''' z is used later as a value in function gen_s, assign the number of iterations
 to the max number of iterations'''
z = num_of_iterations

'''Input from user, ask for criterion to stop the model. If the input is not 
in range, it will ask again'''
while True:
    try:
        crit = int(input("Please choose one criterion to stop this model" + 
                                  ":\n Type 1 to stop when average value stored by"
                                  "  all agents is greater than 70 \n Type 2 to stop when" +
                                  " the range (max-min) is greater than 50\n Type 3"+
                                  " to stop when the min value stored is further more"+
                                  " than 2 std.dev from average\n\n Your choice is: "))
        if crit > 0 and crit < 4:
            break
    except ValueError:
        print('A number is requested. Try again. For example, write 20') 

#Settings for animation
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#List that will store the input which represents the environment
environment = []

#Make a list to create agents
agents = []

#Read the input and import it into environment list
with open('abm\in.txt', newline = '') as f:
    reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

#Check if environment imported correctly
#print(environment)
        

#Visualize the environment list    
'''
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show() 
'''


# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


#Check if agents were created, with x and y coordinates as lentgh 
# of environment array
'''
for i in range(num_of_agents):
    print("Agent N°" + str(i) + " x and y coordinates are: "+ str(agents[i].x) 
          +"," + str( agents[i].y))
'''

#Variable which keep the model running and the animation on
carry_on = True	


#define frame for animation
def update(frame_number):
    """Create each frame for the animation, based in parametrers defined by user.

    Argu -- Assign the criterion selected previously to stop the model running.
    """
    #Clear the figure for the next frame of animation
    fig.clear()
    global carry_on
    #List that will store the values of the agents in each iteration
    storage = []
    

    # In each iteration, agents will move, eat and check its neighbourhood
    for j in range(num_of_iterations):
        #Change the order of agents to avoid artifacts from this model
        random.shuffle(agents)
        #List of data store by each agent
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        storage.append(agents[i].store)
     
    def argu(crit):
        '''Based in the number of criterion selected by user, return the 
        statement to evaluate the stop of the model.
        

        Parameters
        ----------
        crit : Interger between 1 and 3, inclusive.

        Returns
        -------
        Statement to assess when to stop the model.
        '''
        if crit == 1:
            return statistics.mean(storage) >70
        elif crit == 2:
            return max(storage) - min(storage) > 50
        elif crit == 3:
            return min(storage) < (statistics.mean(storage) 
                                   - 2 * statistics.stdev(storage)) 
        
    #Check average data stored in each iteration. Show the model running
    print("average of data stored by agents in this iterarion is " 
          + str(round(statistics.mean(storage))))
    exportdata(storage)
    
    #Calls the function argu and evaluate the statement to stop the model
    if argu(crit):
        carry_on = False
        print("Your input criterion has been met") 
        
    #Display X and Y coordinate of agents in each iteration to create each frame
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        #print(agents[i].x,agents[i].y)
        
    if carry_on == False:
        print("End" + "\nCheck your outputs in your directory to see the results")

    
def gen_function(b = [0]):
    '''Acts like an iteration, defines when to stop the once the number of 
    max iteration has been met.
    

    Parameters
    ----------
    b : Interger. The count start from 0

    Yields
    ------
    When the iter 'a' is greater than the max number of iteration value in 'z',
    the model stop running.

    '''
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a <= z) & (carry_on) :
        yield a			# Returns control and waits next call.
        #print("iteration of" + str(a))
        a = a + 1
        
    if a > z:
        print("End. Your criterion was no met after " + str(z) + "iterations" +
              "\nCheck your outputs in your directory to see the results")        
        
def exportdata (storage):
    '''Export two files: the environment after its interaction with agents, and
    the values stored by of each agents
    

    Parameters
    ----------
    storage : Local list in update fuction

    Returns
    -------
    outputData.csv  : list of data stored by each agent in each iteration
                      (If the model is run more than once, the new values are
                       appen to this file. Change the console if you want a
                       file with only the current results.)
                      
    enviroOut.csv  : 2D list of values that represent the new environment after 
    the model was executed.

    '''
    with open("abm\outputData.csv", "a") as f:
        for data in storage:
            f.write(str(data) + ",")
        f.write("\n")
    
    with open("abm\enviroOut.csv", "w") as f:
        for line in environment:
            for value in line:
                f.write(str(value) + " ")
            f.write("\n")
    
#Display the animation                
animation = matplotlib.animation.FuncAnimation(
    fig, update,frames=gen_function, repeat=False)
matplotlib.pyplot.show()

#importlib.reload(model)
