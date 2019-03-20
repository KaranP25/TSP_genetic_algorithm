import matplotlib.pyplot as plt
from logic.City import City
from logic.SalesmanExpedition import SalesmanExpedition

class Plot:
    def __init__(self, names_list, cordlist_x, cordlist_y):
        self.names_list = names_list
        self.cordlist_x = cordlist_x
        self.cordlist_y = cordlist_y
        
    
    def plot(self):
        plt.xlabel('X-Axis')
        plt.ylabel('Y-Axis')
        plt.plot(self.cordlist_x, self.cordlist_y)

        for i, names_list in enumerate(self.names_list):
            plt.scatter(self.cordlist_x[i], self.cordlist_y[i], color='b')
            plt.text(self.cordlist_x[i]+1.9, self.cordlist_y[i]+1.6, names_list, fontsize=10)
        plt.plot(self.cordlist_x[0], self.cordlist_y[0], 'g', label='Start City', marker='o')
        plt.plot(self.cordlist_x[-1], self.cordlist_y[-1], 'r', label='End City')
        plt.legend(loc="best")

        plt.savefig("output.png", bbox_inches="tight")
        plt.show()
