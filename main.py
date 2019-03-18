import csv
from logic.City import City
from logic.Salesman import Salesman
from logic.Population import Population
from logic.GA import GA

salesman = Salesman()

with open('data/points.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        point = City(row['id'], int(row['x']), int(row['y']))
        salesman.addCity(point)

 # Initialize population
pop = Population(salesman, 100, True);
print(f'Initial distance: {str(pop.getFittest().get_distance())}')

# Evolve population for 50 generations
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
