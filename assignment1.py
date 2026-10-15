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
    time_step = 0.01
    N = int(T_final / time_step)
    variance = 1

    Q_backups = np.zeros((runs, N))

    #2 - Preform R runs
    for run in range(0, runs):    

        Q = np.array([0])
        for t in range (0, N-1):
  
            change = (lambda_arrival - (mu_service *  min(Q[t], C)) * time_step ) 
            noise = variance * np.sqrt(time_step) * np.random.normal(0,1)
            next_Qt = Q[t] + change + noise

            if next_Qt < 0:
                next_Qt = 0

            Q = np.append(Q, next_Qt)

        Q_backups = np.append(Q_backups, Q)

        print(".")
        #print(len(Q))
        #RECOVER SOLUTIONN?
        #PLOT?

    for q in Q_backups:
        print (q)
    mean_Q_len = (1/N) * np.mean(Q_backups)
    stdev_Q_len = np.std(Q_backups, ddof=1)
    mean_occ = (mean_Q_len / C) * 100
    total_runtime = time.time() - execution_start_time
    

    #do calculations


    #print results

    print("Mean queue length...", mean_Q_len)
    print("Stdev queue length...", stdev_Q_len)
    print("Mean occupancy: %....", mean_occ)
    print("Total run time: ... seconds", total_runtime)

    return 0



def main():
    simulateQueue(160, 4., 0.4, 16, 100)


if __name__ == "__main__":
    main()