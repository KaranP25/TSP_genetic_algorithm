import csv
from logic.City import City
from logic.Salesman import Salesman
from logic.Population import Population
from logic.GeneticAlgorithm import GeneticAlgorithm
from plot import Plot

# import and add the distance data
def import_distance():
    distance_salesman = Salesman()

    with open('data/cities_distance.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            id = row['city']
            del row['city']
            distance_dict = {}
            for key, value in row.items() :
                distance_dict[key] = value
            city = City(1, str(id), x=None, y=None, distance_dict=distance_dict)
            distance_salesman.add_city(city)

    return distance_salesman

#import and add the point data
def import_point():
    point_salesman = Salesman()

    with open('data/points.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            point = City(0, row['id'], int(row['x']), int(row['y']))
            point_salesman.add_city(point)

    return point_salesman

def main():
    salesman = Salesman()
    decision = ''
    # user prompt
    while True:
        decision = input("Which data points do you want to use (Type [P] for point data or [D] distance data)?")
        if decision.upper() not in ('P', 'D'):
            print("Not an appropriate choice.")
        else:
            if decision.upper() == 'P':
                salesman = import_point()
            else:
                salesman = import_distance()
            break

    crossover_method = 0
    mutation_method = 0
    # user prompt
    while True:
        decision = input("\nWhich mutation and crossover method? \n(Type [1] for one-point crossover and swap mutation or \n[2] for one-point crossover and scramble mutation \n[3] for two-point crossover and swap mutation) \n[4] for two-point crossover and scamble mutation)?")
        if decision.upper() not in ('1', '2', '3', '4'):
            print("Not an appropriate choice.")
        else:
            if decision == '1':
                crossover_method = 0
                mutation_method = 0
            elif decision == '2':
                crossover_method = 0
                mutation_method = 1
            elif decision == '3':
                crossover_method = 1
                mutation_method = 0
            elif decision == '4':
                crossover_method = 1
                mutation_method = 1
            break

    # Initialize the population
    pop = Population(salesman, 300, True);
    print(f'\nInitial distance: {str(pop.get_fittest().get_distance())}')

    # Evolve the population
    print("Population evolving...Getting the fittest result...")
    ga = GeneticAlgorithm(salesman, mutation_method, crossover_method)
    pop = ga.evolve(pop)
    for i in range(0, 100):
        pop = ga.evolve(pop)
    
    # Print final results
    print("Evolving Population Complete\n")
    print(f'Minimum distance: {str(pop.get_fittest().get_distance())}')
    print(f'Fittest Solution: {pop.get_fittest()}')
    print(f'\nFitness function: {pop.get_fittest().get_fitness()}')

    # user prompt to plot
    while True:
        prompt = input("Do you want to plot the data (Type [Y] for yes or [N] no)?")
        if prompt.upper() not in ('Y', 'N'):
            print("Not an appropriate choice.")
        else:
            if prompt.upper() == 'Y':
                fittest_id = [city.get_id() for city in pop.get_fittest().get_tour()]
                fittest_x = [city.get_x() for city in pop.get_fittest().get_tour()]
                fittest_y = [city.get_y() for city in pop.get_fittest().get_tour()]

                fittest_plot = Plot(fittest_id, fittest_x, fittest_y)
                fittest_plot.plot()
            else:
                pass
            break

if __name__ == '__main__':
    main()