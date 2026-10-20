import numpy as np
import matplotlib as plt
import time

# T_final is final time T = (N-1)*timestep
# lamba_arrival is valye of lambda (job arrival rate)
# mu_service is value of mew (service rate)
# C - number of processors
# runs - num of independant random runs to be preformed

def simulateQueue(T_final, lambda_arrival, mu_service, C, runs=1):

    execution_start_time = time.time()

    #1 initialise
    time_step = 0.01 # time step
    N = int(T_final / time_step) + 1 # 
    sigma = 1

    Q_backups = []
    Q0 = 0

    #2 - Preform R runs
    for r in range(0, runs):    

        #initialise current Q
        Q = np.array([Q0])

        # 3 - Preform time loop
        for t in range (0, N-1):

            #3 - Update Qt+1 from Qt
            change = (lambda_arrival - (mu_service *  min(Q[t], C)) )* time_step 
            noise = sigma * np.sqrt(time_step) * np.random.normal(0,1) #with np.normal being ( loc(mean)=0 and scale(sigma)=1 )
            next_Qt = Q[t] + change + noise

            #3 - if negative  bthen set equal to 0
            if next_Qt < 0:
                next_Qt = 0

            #next
            Q = np.append(Q, next_Qt)

        Q_backups.append(Q)
        print(".")
  
        #print(len(Q))
        #RECOVER SOLUTIONN?
        #PLOT?



    mean_Q_len = 0
    stdev_Q_len = 0
    mean_occ = 0
    total_runtime = 0

    mean_Q_len = np.mean(Q_backups)
    stdev_Q_len = np.std(Q_backups, ddof=1) #only need to caluclate for one 1 bc they are all the same length?
    mean_occ = (mean_Q_len / C) * 100 #convert to percentage
    total_runtime = time.time() - execution_start_time

    #print results
    print("Queue statistics over", runs, "runs.")
    print(f"Mean queue length: {mean_Q_len:.2f}")
    print(f"Stdev queue length: {stdev_Q_len:.2f}")
    print(f"Mean occupancy: {mean_occ:.2f}%")
    print(f"Total run time: {total_runtime:.2f} seconds")
    return 0


def plot():
    # Initialise a single plot before the for-loop
    plt.figure()

    # Separate plot for each run in the same figure
    plt.plot(time_points, Q, linewidth=0.8, alpha=0.7)

    # Define the plot elements like axis labels
    plt.xlabel('Time (minutes)')
    plt.ylabel('Queue length')
    plt.title('SDE queue simulation (' + str(runs) + ' runs)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Export plot as a PNG image
    plt.savefig(...)

def main():
    print("Task A:")
    simulateQueue(160, 4., 0.4, 16, 100)

    print("/nTask B:")
    simulateQueue(120, 400/120, 1/5, 32, 5)
    #PLOT IS MANDATORY

if __name__ == "__main__":
    main()