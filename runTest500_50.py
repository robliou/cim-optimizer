#Initialization and Imports
import sys
import numpy as np

from pathlib import Path
sys.path.append(str(Path.cwd()) + "\\..\\") # append repo to list of search directories

from cim_optimizer.solve_Ising import *
from cim_optimizer.CIM_helper import brute_force
import time
start_time = time.perf_counter()
import sys
sys.path.append("./data")

import convert_to_matrix_500_50 

matrix_raw = np.zeros((500, 500))
# Loop through the list of tuples and set corresponding positions to 1
for pos in convert_to_matrix_500_50.lst:
    row = pos[0]
    col = pos[1]
    val = pos[2]
    matrix_raw[row][col] = val

# Print the matrix
print('this is matrix_raw',matrix_raw)


# Save the full matrix to a text file
np.savetxt("full_matrix.txt", matrix_raw, fmt="%d")

matrix2 = -np.array(matrix_raw)

#matrix = -np.array([
  #              [0, 0, 0, 1, 0],
   #             [0, 0, 1, 1, 1],
    #            [0, 1, 0, 1, 1],
     #           [1, 1, 1, 0, 0],
      #          [0, 1, 1, 0, 0],
       #      ])

# 20 spin MAXCUT problem
N = 500
mc_id = 1 # select first example of 20 spin MAXCUT problem
#J = - np.load(instance_path_str_MAXCUT + f"MC50_N={N}_{mc_id}.npz") # load J matrix for 50% density MAX-CUT problem
gamma = 0.010 # set gamma hyperparameter

#test = Ising(matrix2).solve(cac_gamma=gamma, hyperparameters_randomtune = False)


#print("Time Elapsed: {} seconds".format(test.result.time))
#print("Minimum Energy Achieved: {}".format(test.result.lowest_energy))
#np.set_printoptions(threshold=10, edgeitems=1)
#print("Energy Evolution: {}".format(test.result.energy_evolution))
#print("Spin Evolution: {}".format(test.result.spin_trajectories))
#test.result.plot_spin_trajectories(plot_type="spins")
#test.result.plot_spin_trajectories(plot_type="energy")

timestep_count = 1000
my_feedback_schedule = lambda x: np.sin(x/20)#torch.sin(torch.arange(timestep_count))
#test = Ising(matrix2).solve(cac_gamma=gamma, num_runs=5, num_timesteps_per_run = timestep_count, custom_feedback_schedule=my_feedback_schedule, #hyperparameters_randomtune = False)

#timestep_count = 5000
#ground_state_ising_energy = -29.0
#my_feedback_schedule = lambda x: np.sin(x/33)
#test = Ising(matrix2).solve(cac_gamma=gamma, num_runs=5, target_energy=ground_state_ising_energy, num_timesteps_per_run = timestep_count,
#                      custom_feedback_schedule=my_feedback_schedule, hyperparameters_randomtune = False)

#print(f"Number of discrete steps (roundtrips): {timestep_count}")
#roundtrip_time = 1.6e-6 #Roundtrip time in seconds, as reported in (https://doi.org/10.1126/science.aah5178)
#print(f"Roundtrip time: {roundtrip_time} second")
#print(f"Total CIM runtime: {timestep_count*roundtrip_time} second(s)")




def num_cut_edges(initial_matrix, ground_state_solution):
    num_edges = 0
    for i in range(len(initial_matrix)):
        for j in range(i+1, len(initial_matrix)):
            if initial_matrix[i][j] == 1 and ground_state_solution[i]*ground_state_solution[j] == -1:
                num_edges += 1
    return num_edges

#num_edges = num_cut_edges(matrix_raw, best_cut)

#print("Number of cut edges: ", num_edges)

# Create an empty array
my_array = []

final_time=0

for i in range(100):
    start_time = time.perf_counter()
    test = Ising(matrix2).solve(cac_gamma=gamma, num_runs=1, num_timesteps_per_run = timestep_count, custom_feedback_schedule=my_feedback_schedule)
    best_cut = test.result.lowest_energy_spin_config


    num_edges = num_cut_edges(matrix_raw, best_cut)
    final_time = time.perf_counter() - start_time 

    my_array.append((num_edges, final_time))


my_array = np.array(my_array)

# Save the array as a NumPy array locally
np.save('my_array.npy', my_array)


# Save the array as a text file
np.savetxt('my_array.txt', my_array) 

print("my_array ", my_array)


print("Number of cut edges: ", num_edges)


# Extract the x and y coordinates from the array of tuples
x = my_array[:, 0]
y = my_array[:, 1]

# Plot the points
plt.scatter(x, y)
plt.xlabel('# cuts ')
plt.ylabel('time in seconds')

# Calculate the average of the y-coordinates
average_x = np.mean(x)

average_y = np.mean(y)

# Print the average of the y-coordinates
print("The average of the x-axis values is:", average_x)

print("The average of the y-axis values is:", average_y)


# Show the plot
plt.show()