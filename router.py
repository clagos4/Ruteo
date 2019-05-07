import pandas as pd

GRID_WIDTH = 30000
GRID_HEIGHT = 30000

if __name__ == '__main__':

    data = pd.read_csv('./Dataset Denunicias 2018.csv', delimiter=';')

    data = data.values.tolist()
    print(data)
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for delation in range(len(data)):
      add_point(grid, delation)
