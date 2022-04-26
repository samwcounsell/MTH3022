from scipy.stats import bernoulli
import matplotlib.pyplot as plt

# Parameters for the simulation; n = people at each stage, i = initial infections
# p is probability of infection to each person at the next stage, sim_number is number of simulations
n = 2
i = n
p = 0.5
sim_number = 1000

# List to store length of each simulation
sim_list = [0] * sim_number

# Function to run infection simulations
for sim in range(sim_number):

    # count is length of the simulation, i is number of initially infected people at stage 0,
    # c_inf is the number of people who have become infected in the next stage
    count = 0
    i = n
    c_inf = 0

    # Simulation continues as long as at least one person is still infected at the next stage
    while i > 0:

        new_i = 0

        # Each person at the next node is given the chance to be infected by each currently infected person
        for j in range(n):

            # Bernoulli trial to randomise if a person becomes infected
            for k in range(i):
                infected = bernoulli.rvs(p, size=1)
                c_inf = c_inf + infected

            # If they catch the disease from at least one person at the current stage, they become infected at the
            # next stage
            if c_inf > 0:
                new_i = new_i + 1

            # Re-setting the parameters
            c_inf = 0

        # Updating parameters for the next stage of the simulation
        i = new_i
        count = count + 1

    # Adding the data to the list
    sim_list[sim] = count


# Calculating the mean length of the infection chain
mean = sum(sim_list) / 1000
print(f'Mean length of infection chain is {mean}')

# Plotting histogram of the average length of the infection chain
plt.hist(sim_list, bins = int(round(sim_number / 10)))
plt.title(f'Corridor with {n} people at each section')
plt.show()
