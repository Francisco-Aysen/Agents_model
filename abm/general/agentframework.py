# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:19:19 2022

@author: FMP
"""

import random


class Agent():
    ''' Provide properties and functions to be called in ABM.
    
    __init__ -- method for propierties of each agent
    
    n_row -- count the number of rows, return the Y lenght
    
    n_column -- count the number of columns, return the x lenght
    
    get, setx, gety, set -- mutator and accesor for X and Y
    
    move -- the agent moves randomly one position both in X and Y dimentions
    
    eat --  the agent eats 10 from environmnet and stores it. If an agent eat 
            until 110, it will 'sick-up' 100 back to the environment in the 
            next move
    
    __str__ -- When and agent is called, print X, Y and its data stored
    
    distance between -- calcularte the euclidean distance between two agents
    
    share_with_neighbours -- check if there is another agent in the 
                            neighbourhood and change the store of both agent
                            to their average's'
    
    '''
    
    def __init__(self, environment, agents):
        '''blueprint for creating agents
        

        Parameters
        ----------
        environment : List imported from in.txt

        agents : List created in model that contains all the agents.
        '''
        self.environment = environment
        self.agents = agents
        self.y_length = len(environment)
        self.x_length = len(environment[0])
        self._y = random.randint(0, self.y_length)
        self._x = random.randint(0, self.x_length)        
        self.store = 0
        self.pair_dist = []
        
    def n_row(self):
        return self.y_length
    
    def n_column(self):
        return self.x_length
        
    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value
        
    x = property(getx, setx, "I'm the 'x' property.")   
    
    def gety(self):
        return self._y
    
    def sety(self, value):
        self._y = value
        
    y = property(gety, sety, "I'm the 'y' property.")
    
    def move(self):
        '''the agent moves randomly one position both in X and Y dimentions

        Returns
        -------
        New X and Y position of each agent.

        '''
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.y_length
        else:
            self.y = (self.y - 1) % self.y_length
        if random.random() < 0.5:
            self.x = (self.x + 1) % self.x_length
        else:
            self.x = (self.x - 1) % self.x_length
            
    def eat(self):
        '''the agent eats 10 from environmnet and stores it. If an agent eat 
                until 110, it will 'sick-up' 100 back to the environment in 
                the next move
        
        Returns
        -------
        New value for store of each agent.

        '''
        if self.store <= 100:
            if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -=10
                self.store += 10
            else:
                 self.rest = self.environment[self.y][self.x]
                 self.environment[self.y][self.x] -=  self.rest
                 self.store += self.rest
        else:
            self.sick_up = self.store - 100
            self.environment[self.y][self.x] += self.sick_up
            self.store -= 100
             
    def __str__(self):
        return "(x = " + str(self.x) + ", y = " + str(self.y)
        +  ", data store = " + str(self.store) + ")"
    
    def distance_between(self, agent):
        '''calculate the euclidean distance between two agents
        

        Parameters
        ----------
        agent : List of all agents in model

        Returns
        -------
        Distance between each agent and the rest of agents.

        '''
        return (((self.x - agent.x)**2) +
            ((self.y - agent.y)**2))**0.5
       
    def share_with_neighbours(self, neighbourhood):
        '''check if there is another agent in the neighbourhood and change 
        the store of both agent to their average's'
        

        Parameters
        ----------
        neighbourhood : Integer defined by the user to set the search area

        Returns
        -------
        New values of store of agent if there's another in the search area.

        '''
        # Loop through the agents in self.agents.
        for agent in self.agents:
            distance = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                average = (self.store + agent.store) / 2
                self.store = average
                agent.store = average
                #print("sharing " + str(distance) + " " + str(average))
