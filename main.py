import csv
from logic.City import City
from logic.Salesman import Salesman
from logic.Population import Population
from logic.GA import GA

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
            distance_salesman.addCity(city)

    return distance_salesman

def import_point():
    point_salesman = Salesman()

    with open('data/points.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            point = City(0, row['id'], int(row['x']), int(row['y']))
            point_salesman.addCity(point)

    return point_salesman

salesman = Salesman()

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

 # Initialize the population
pop = Population(salesman, 300, True);
print(f'Initial distance: {str(pop.getFittest().get_distance())}')

# Evolve the population
print("Population evolving...Getting the fittest result...")
ga = GA(salesman)
pop = ga.evolvePopulation(pop)
for i in range(0, 100):
    pop = ga.evolvePopulation(pop)

# Print final results
print("Evolving Population Complete\n")
print(f'Minimum distance: {str(pop.getFittest().get_distance())}')
print(f'Fittest Solution: {pop.getFittest()}')
print(f'\nFitness function: {pop.getFittest().get_fitness()}')
