import pdb
from helpers import normalize, blur
import numpy as np

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    beliefs_np=np.array(beliefs)
    new_beliefs = np.zeros(beliefs_np.shape)
  

    #
    # TODO - implement this in part 2
    for i in range(beliefs_np.shape[0]):
        for j in range(beliefs_np.shape[1]):
            e=grid[i]
            e=e[j]
            hit=e==color
            new_beliefs[i][j]=beliefs_np[i][j]*(hit*p_hit+(1-hit)*p_miss)
       
    #
    new_beliefs=new_beliefs/np.sum(new_beliefs)
    return new_beliefs.tolist()

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i - dy ) % width
            new_j = (j - dx ) % height
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)