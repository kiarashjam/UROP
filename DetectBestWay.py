import secrets
import random
import matplotlib.pyplot as plt

from euclid import Vector3
from ga.chromosome_elem import ChromosomeElem
from track_generator.command import Command
from track_generator.generator import generate_track
from scipy.spatial import distance
from Testing_point import testing_track

start_position = Vector3(x=49.7, y=0.5, z=50.0)
node_position_list = list()

amount = 200
last_points = start_position





def generate_genome(last_point) :

    valid = True
    while valid:
        commands = ["s", "r", "l"]
        direction = secrets.choice(commands)
        if (direction  == "s") :
            degree = 0
            chromosome_element = [ChromosomeElem(command=Command.S, value=1)]
        elif (direction  == "r"):
            degree = random.uniform(1, 180)
            chromosome_element = [ChromosomeElem(command=Command.DY, value=degree),
                                  ChromosomeElem(command=Command.R, value=1)]
        elif (direction  == "l"):
            degree = random.uniform(1, 180)
            chromosome_element = [ChromosomeElem(command=Command.DY, value=degree),
                                  ChromosomeElem(command=Command.L, value=1)]

        end_point = testing_track(chromosome_element, last_point)


        valid = False
        for node in node_position_list:
            dst = distance.euclidean(node, end_point)
            if dst < 1:
                valid = True



    return [direction,degree], end_point


# generate a population
def generate_population():
    node_position_list.clear()
    population = list()
    # first direction should be straight
    node_position_list.append(start_position)
    population.append(["s",0])
    last_point = testing_track([ChromosomeElem(command=Command.S, value=1)],start_position)
    node_position_list.append(last_point)

    # all the 17 commands generation
    i=0
    while i < 17:
        new_genome, new_position_node= generate_genome(last_point)
        last_point = new_position_node
        node_position_list.append(new_position_node)
        population.append(new_genome)
        i = i+1
    # the last one also should be straight command
    return population

def fitness(population):

    end_point , track_points = executor(population)
    dst = distance.euclidean(start_position, end_point)
    return dst, track_points
#################################
def mutation (population):
    index = random.randrange(len(population))
    population[index]= generate_genome(last_points)
    return population

##########################33
def single_point_crossover(a,b):
    if len(a) != len(b):
        raise ValueError("genome a , b must be of same lenght ")
    # if the length is too low

    length = len(a)
    if length < 2:
        return a, b
    p = random.randint(1, length - 1)
    rtl = a[0:p] + b[p:], b[0:p], a[p:]
    return rtl

#########################


def executor(commands):
    chromosome_elements =list()
    for command , degree in commands:
        if command == "s":
            chromosome_elements.append(ChromosomeElem(command=Command.S, value=1))
        elif command == "l":
            chromosome_elements.append(ChromosomeElem(command=Command.DY, value=degree))
            chromosome_elements.append(ChromosomeElem(command=Command.L, value=1))
        elif command == "r":
            chromosome_elements.append(ChromosomeElem(command=Command.DY, value=degree))
            chromosome_elements.append(ChromosomeElem(command=Command.R, value=1))


    track_points, end_point = generate_track(chromosome_elements=chromosome_elements)
    return end_point, track_points

def  drawing_plot(track_points):
    plot_x = [track_point.x for track_point in track_points]
    plot_y = [track_point.y for track_point in track_points]
    i = 1
    while i < len(plot_x):
        if  i ==1:
            colors = "#0" +str(i * 5) + "0" + str(i * 5) + "0" + str(i * 5)
        elif 2 < i < 20:
            colors = "#"+str(i * 5)+str(i * 5)+ str(i * 5)
        else:
            colors = "#"+ str(i)+str(i)+str(i)
        plt.scatter(plot_x[i], plot_y[i], color=colors)
        i = i + 1
    plt.show()


def run_evolutaion():
    i=0
    all_population  = list()
    while i < amount:
        population = generate_population()
        distance ,track_points = fitness(population)
        all_population.append([distance, track_points])
        i = i + 1
    min_distance = all_population[0][0]
    points = all_population[0][1]
    for node in all_population:
        if (min_distance > node[0]):
            points = node[1]
            min_distance = node[0]
    print("The lowest distance in amount of "+str(amount)+" is  = " +str(min_distance))
    drawing_plot(points)



run_evolutaion()
