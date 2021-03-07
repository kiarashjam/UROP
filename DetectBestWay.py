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
        # for node in node_position_list:
        #     dst = distance.euclidean(node, end_point)
        #     if dst < 1:
        #         valid = True



    return [direction,degree], end_point


# generate a population
def generate_population() :
    print("step 1")
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
        # print("step " + str(i))
        new_genome, new_position_node= generate_genome(last_point)
        last_point = new_position_node
        node_position_list.append(new_position_node)
        population.append(new_genome)
        i = i+1
    # the last one also should be straight command
    # population.append(["s", 0])
    return population

def fitness(population):

    end_point , track_points = executor(population)
    dst = distance.euclidean(start_position, end_point)
    return dst, track_points


#################################
# def mutation (population) :
#     print("sa9")
#     index = random.randrange(len(population))
#     population[index]= generate_genome()
#     print("s13")
#     return population

##########################33
def single_point_crossover(a,b):
    if len(a) != len(b):
        raise ValueError("genome a , b must be of same lenght ")
    # if the length is too low

    length = len(a)
    if length < 2 :
        return a, b
    p = random.randint(1, length - 1)
    rtl = a[0:p] + b[p:], b[0:p], a[p:]
    return rtl

#########################

# def run_evolutaion(
#         populate_func,
#         fitness_func,
#         fitness_limit,
#         selection_fun = selection_pair,
#         crossover_func = single_point_crossover,
#         mutation_func= mutation,
#         generation_limit = 100,):
#
#     population = generate_population()
#     for i in range(generation_limit):
#
#         population = sorted(
#             population,
#             key=lambda genome: fitness_func(genome),
#             reverse=True
#         )
#         if fitness_func(population[0]) >= fitness_limit:
#             break
#         next_generation = population[0:2]
#         print("s9")
#
#         for j in range(int(len(population)/2) - 1):
#             print("rang = " + str(range(int(len(population)/2)) ))
#             print(j)
#             print("s10")
#             # print ("here1 ")
#             # print("run evaluation + population" +str(population))
#             # print("run evaluation +fitness " + str(fitness_func))
#             parents = selection_fun(population, fitness_func)
#             print("sa10")
#             offspring_a, offspring_b = crossover_func(parents[0], parents[1])
#             print("s15")
#             offspring_a = mutation_func(offspring_a)
#             print("sa16")
#             offspring_b = mutation_func(offspring_b)
#             print("sa17")
#             next_generation +=[offspring_a,offspring_b]
#             print("sa18")
#         population = next_generation
#         print("sa19")
#     population = sorted(
#         population,
#         key=lambda genome: fitness_func(genome),
#         reverse=True
#     )
#     print("s9")
#     return population, i


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
        # print("distance = " + str(distance) + " / number " + str(i))
        # print("plot = " + str(type(plt)) + " / number " + str(i))
        i = i + 1
    min_distance = all_population[0][0]
    # print(all_population[0][1])

    points = all_population[0][1]
    for node in all_population:
        # print("node zero = "+  str(node[0]))
        # print("min distance = " +str(min_distance))
        if (min_distance < node[0]):
            points = node[1]
            min_distance = node[0]
    drawing_plot(points)





run_evolutaion()

# s =fitness(generate_population())
# print(s)
# distance, end_point = generate_genome()
# print(end_point)
# print(distance)
