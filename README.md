# purpose of the project

This operator is about to find the minimum and the maximum version of the distance with 19 commands. 

# Requirments

At first, install the requirements and dependencies with the command. : 

```pip install -r requirements.txt```



# how to run the test


With the command below, you can run the whole program.

```python DetectBestWay.py```



As the minimum distance, print the least distance possible in their solution.


it also shows the maximum distance in their build population in the plot:

![alt text](https://github.com/kiarashjam/UROP/blob/master/lowest_distance.png)


Also, it can generate the plot for the minimum distance.


# how the system work:
## 1- generate_genome()

In this function, it builds one command as the genome. It chooses randomly from left, right, and straight commands. Then if it is straight, it chooses zero degrees for it. Suppose the command is right or left. It will pick a random degree for the command.


also in the last part, which considers the validity of the genome 

If it is valid, it should have the distance "one" from all nodes; otherwise, it returns the False validity, making the function make another genome. It will iterates until the genome finds the valid one.


## 2- generate_population()

The population makes the series of commands whose length of the command is 19 (defined in the constraint).

The first one and last one must be straight, so it searches for the other genome to complete the population list.


## 3- fitness()

In this function, it will return the last point and starting point of the population.


## 4- mutation()

In the mutation, we change one of the population's commands and make a new commands list.


## 5 -single_point_crossover()

In this part, the two populations will cut in half and make the new generation from itself.


## 6 - executor()

The executor will execute all the commands on the ga classes and return the points' coordinates after the commands.


## 7 - drawing_plot()

This function draws the plot with the coordinates.

The beginning has lighter color. However,  the ending point has a darker color, as you can see in figure 1.

# outcome

The outcome will be the maximum distance of the commands and the minimum distance for the commands with the iterate amount = 200.



# modifying the source code

This class modifies the generator for the own purpose.



