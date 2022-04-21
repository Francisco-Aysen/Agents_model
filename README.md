# Agents_model

## Brief description of this model
This model tries to reproduce the behaviour of agents wandering through a limited space, interacting with their environment and also with other agents.
In each move, each agent moves one step in both X and Y axis, eats 10 points from the cell on which it's located, and then, search in given neighbourhood 
to other agents. If one agent is placed in that area, the agents change their store points to the average of their values.
Each agent can only eat points from the environment up to 110 points. Once this values has been reached, on the next move, the agent will sick-up 100 points 
back to the environment.

This model can be useful when researching if sharing points between agents helps to improve the total points by all the agents, and if increasing or decreasing the
neighbourhood affects the emergence of inequalities among agents.

## Content list

This repository consist of a folder named 'abm', and two files, this README file and a License file.

Folder abm has two subfolders: 'model' and 'general' and also three files: in.txt, enviroOut.csv and outputData.csv. The text file is a grid of data, simillar to a 
raster of elevation which describes the environment. Both .csv files are outputs of the model; enviroOut shows the new enviroment after the interaction of agents, 
and output data contais the values stored by each agents through each iteration.

In 'model', you can find the main script of this program 'model.py'. This module is expected to be run as a script in cmd. When doing so, it will ask fot the main values to 
set the model, such as: number of agents, number of maximum iteration, neighbourhood and a criterion to stop the model (more details in 'How to run this program').

In 'general', you will find the module 'agentframework.py', which contains the class and functions called in this model. 

## How to run this program

Download this code as a zip folder. Unzip it and you will have a folder named 'Agents_model-main'. Shift and right-clic on this folder and open the Command Prompt.
Write 'Python', and push Enter. Then 'import abm.model.model' and Enter. This will import the module model.py, and will ask you to enter the following parametres:
  _number of agents: this value must be an interger.
  _number of max iterations to run in this model: this value must be an interger.
  _neigbourhood: this value must be an interger.
  _criterion to stop the model: this valiue must be an interger among 1 and 3, inclusive.

The criterion to stop the model can be of the followings:
  _1 to stop when average value stored by all agents is greater than 70
  _2 to stop when the range (max-min) is greater than 50
  _3 to stop when the min value stored is further more than 2 std.dev from average
  
If you type a letter instead of an interger, or an interger out of range in the criterion input, the program will ask you again to write a proper input.
  
## Results

After the model has been set, it will start running. A window will pop-up, representing the location and movement of agents. Also, in the command, the following text
will describe the average data stored by all agents in each interation (i.e 'average of data stored by agents in this iterarion is 50').

If you criterion has been met, the model will stop runing, and the following text will appear:

'Your input criterion has been met
End
Check your outputs in your directory to see the results'

Othewise,  the model will stop runing when the maximum number of iteration has been reached, and the following text will appear:

'End. Your criterion was no met after 9 iterations
Check your outputs in your directory to see the results'

The outputs enviroOut.csv and outputData.csv will be created into abm folder. 

## Known issues

Unfortunately, this model cannot be executed inmediately after each run. You will have to type 'quit()', and after that, type 'import abm.model.model' again.

## Further developments

The text output in each iteration could change according to the criterion selected. Currently, in each iteration, the average value is represented, which is
related to criterion n°1. In further versions, the prompt could represent min and max values if criterion n°2 were selected or min value and 2 std.dev from average
in criterion n°3.

## License

The present program is under MIT License.
