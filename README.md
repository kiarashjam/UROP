# Purpose of the project

This operator is about to find the minimum and the maximum version of the distance with 19 commands. 
This operator is finding the minimum and maximum distance versions with 19 commands.

# Requirments

At first, install the requirements and dependencies with the command. : 
First, install the requirements and dependencies with the commands :
```pip install -r requirements.txt```



# How to run the test


With the following command,be able to run the entire program.

```python DetectBestWay.py```

As a minimum distance, print the shortest possible distance in their solution.

Also shows the minimum distance in the population of in the form of the plot. as an example:
![alt text](https://github.com/kiarashjam/UROP/blob/master/lowest_distance.png)


Also, it can generate the plot for the minimum distance.
Also, it can create the plot for the minimum distance.

# How the System Work:
## 1- generate_genome()

In this function, it builds one command as the genome. It chooses randomly from left, right, and straight commands. Then if it is straight, it chooses zero degrees for it. Suppose the command is right or left. It will pick a random degree for the command.

In this function, it creates a command as a genome. Selects commands randomly from left, right and straight. Then if it is straight, it chooses zero degrees for it. Suppose the command is right or left. This will select a random degree for the command.

also in the last part, which considers the validity of the genome 
Also in the last part, which considers the validity of the genome.

If it is valid, it should have the distance "one" from all nodes; otherwise, it returns the False validity, making the function make another genome. It will iterates until the genome finds the valid one.(for avoiding the loop)

If valid, it must be "one" away from all nodes. Otherwise, it returns the False validation and causes this function to create another genome. Will be repeated until the genome finds a valid genome. (To prevent loop)

## 2- generate_population()

The population makes the series of commands that is the length of the command 19 (defined in the constraint).
The first and last one must be straight, so it searches for the other genome to complete the population list.

## 3- fitness()

In this function, it will return the last point and starting point of the population.
In this function, it returns the last point and the starting point of the population.

## 4- mutation()

In the mutation, we change one of the population's commands and create a list of new commands.

## 5 -single_point_crossover()

In this part, the two populations will cut in half and make the new generation from itself.
In this part, the two populations are divided in half and form a new generation.

## 6 - executor()

The executor will execute all the commands on the ga classes and return the points' coordinates after the commands.
The executor executes all the commands in the classes ga and returns the coordinates of the points after the commands.

## 7 - drawing_plot()

This function draws the plot with the coordinates.

The beginning has lighter color. However,  the ending point has a darker color, as you can see in figure 1.
As you can see in Figure 1, at the beginning,it has a lighter color, the end points are darker in color.
# Outcome

The outcome will be the maximum distance of the commands and the minimum distance for the commands with the iterate amount = 200.
The result will be the maximum command spacing and the minimum command spacing with the value of repetition = 200.


# Modifying the Source Code

This class modifies the generator for the own purpose.



