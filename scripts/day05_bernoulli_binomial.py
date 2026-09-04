'''
Implementing bernoulli and binomial simulators and their comparisons
'''
import numpy as np

np.random.seed(42) #for reproducible results 

def bernoulli_distribution(prob, num):
    # think of uniform random numbers generated as throwing a dart they are just numbers not probabilities
    if prob <= 0 or num <= 0:
        raise(ValueError)
    
    samples = np.random.uniform(0,1,num)
    values = []
    # for the random numbers we decide on the basis of prob as a percentage what percentage of outcomes would actually count as success(1) or failure(0) so for 0.3 prob 30% of outputs are only success so below 0.3 we say it is a success
    for sample in samples:
        if sample <= prob:
            values.append(1)
        else: 
            values.append(0)

    # one shot numpy implementation is also possible directly comparing the whole array which returns true/false which can be converted to 0/1 by using astype(int)
    # final_value = (samples <= prob).astype(int)

    return values


def binomial_sampler(prob, n_trials, num_repeat):
    if prob <= 0 or n_trials <= 0 or num_repeat <=0:
            raise(ValueError)
     
    samples = []
    
    for i in range(0, num_repeat, 1):
        total = 0
        value = bernoulli_distribution(prob, n_trials)
        for val in value: 
            total += val
        # one liner
        # sum = np.sum(value)

        samples.append(total)
    
    return samples

def average(samples):
    
    average = 0
    total = 0
    for sample in samples: 
        total += sample
    average = total / len(samples)

    return average

def standard_deviation(samples):
    avg = average(samples)
    sigma = 0
    for sample in samples:
        diff_squared = (sample - avg)**2
        sigma += diff_squared
    # std = (sigma/len(samples))**(1/2)
    std = np.sqrt(sigma/len(samples))

    return std

def variance(samples):
    avg = average(samples)
    sigma = 0
    for sample in samples: 
        diff_squared = (sample - avg)**2
        sigma += diff_squared

    var = sigma/len(samples)

    return var


# now taking inputs and verifying 
print("="*100)
print("Bernoulli and Binomial sampling simulator")
print("="*100)
success_prob = float(input("\nEnter the success probability (value of p) = "))
num_trials = int(input("\nEnter the number of trials to be performed (value of n) = "))
num_repeat = int(input("\nEnter the number of simulations to be performed = "))
samples_arr_bernoulli = bernoulli_distribution(success_prob, num_repeat) #num_repeat is used because giving it a larger number of trials will generally be a smaller number so approximation might not be good enough for the bernoulli distribution
samples_arr_binomial = binomial_sampler(success_prob, num_trials, num_repeat)
print("="*100)
print("Manually, the value of p is: ", success_prob)
print("Manually, the value of pq is: ", success_prob*(1-success_prob))
print("Manually, the value of np is : ", success_prob*num_trials)
print("Manually, the value of npq is : ", success_prob*(1-success_prob)*num_trials)

print("="*100)

print(f"\nThe average for bernoulli computed directly is: {np.mean(samples_arr_bernoulli)}")
print("="*100)
print(f"\nThe average for binomial computed directly is: {np.mean(samples_arr_binomial)}")
print("="*100)
print(f"\nThe average for bernoulli computed by the manual function is: {average(samples_arr_bernoulli)}")
print("="*100)
print(f"\nThe average for binomial computed by the manual function is: {average(samples_arr_binomial)}")
print("="*100)
print("="*100)
print(f"\nThe standard deviation for bernoulli computed directly is: {np.std(samples_arr_bernoulli)}")
print("="*100)
print(f"\nThe standard deviation for binomial computed directly is: {np.std(samples_arr_binomial)}")
print("="*100)
print(f"\nThe standard deviation for bernoulli computed by the manual function is: {standard_deviation(samples_arr_bernoulli)}")
print("="*100)
print(f"\nThe standard deviation for binomial computed by the manual function is: {standard_deviation(samples_arr_binomial)}")
print("="*100)
print("="*100)
print(f"\nThe variance for bernoulli computed directly is: {np.var(samples_arr_bernoulli)}")
print("="*100)
print(f"\nThe variance for binomial computed directly is: {np.var(samples_arr_binomial)}")
print("="*100)
print(f"\nThe variance for bernoulli by the manual function is: {variance(samples_arr_bernoulli)}")
print("="*100)
print(f"\nThe variance for binomial by the manual function is: {variance(samples_arr_binomial)}")
print("="*100)


    



    

