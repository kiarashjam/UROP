# Purpose of the project
The goall is to simulate "the Developing Self-Driving Car Autopilots using Reinforcement Learning Algorithms" by implementing a Genetic Algorithm.
The code must generate nearby tracks that create the path from start of the instructions' list.
This operator is finding the start and minimum distance with following 19 commands.

# Requirments

First, install the requirements and dependencies with the commands:

```pip install -r requirements.txt```

# How to run the test

With the following command, be able to run the entire program:

```python DetectBestWay.py```

As a minimum distance, print the shortest possible distance in their solution.

It also shows the minimum distance in the population in the form of the plot. as an example:
![alt text](https://github.com/kiarashjam/UROP/blob/master/lowest_distance.png)


# How the System Work:
## 1- generate_genome()



In this function, it creates a command as a genome. Selects commands randomly from left, right, and straight. Then if it is straight, it chooses zero degrees for it. Suppose the command is right or left. Will select a random degree for the command.

Also, in the last part, it is considered the validity of the genome.

If it is valid, it should have the distance "one" from all nodes; otherwise, it returns the False validation and causes this function to create another genome. It will iterates until the genome finds the valid one. (for preventing the loop)


## 2- generate_population()

The population makes the series of commands that is the length of the command 19 (defined in the constraint).

The first and last ones must be straight, so it searches for the other genome to complete the population list.

## 3- fitness()

In this function, it returns the last point and the starting point of the population.

## 4- mutation()

In the mutation, we change one of the population's commands and create a list of new commands.

## 5 -single_point_crossover()

In this part, the two populations are divided in half and form a new generation.

## 6 - executor()

The executor executes all the commands in the classes ga and returns the points' coordinates after the commands.

## 7 - drawing_plot()

This function draws the plot with the coordinates.
As you can see in Figure 1, in the beginning, it has a lighter color; the endpoints are darker in color.

# Outcome

The result will be the maximum command spacing and the minimum command spacing with repetition = 200.


# Modifying the Source Code

This class modifies the generator for the own purpose.



