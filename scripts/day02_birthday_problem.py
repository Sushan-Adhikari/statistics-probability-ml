# solving birthday problem in probability
'''
it asks this question: what must be the minimum number of people in a room such that there is more than 50% chance that two or more people share a birthday
suppose for n people : the total count of interactions would be : 
(n-1) + (n-2) + ... + 3 + 2 + 1 = n(n-1)/2

we want: 
P(>=2 sharing a birthday) = P( person 1 and 2 share a birthday) AND P( person 1 and person 3 share a birthday ) AND P(person 1 and person 4 share a birthday )........ it goes on and on and it is very tedious

instead let's use this shortcut:
P(>=2 sharing a birthday) = 1 - P(no two people sharing a birthday)

for two people not sharing a birthday it is comparatively easy: 

for the first person he has 365 out of 365 choices, the second person has 364 out of 365 choices so that he/she doesn't collide with the first one and so on...
in general it would be (365 - n ) / 365
'''

def birthday_probability(n):
    n = int(n)
    # have to make sure the product isn't initialized to zero as it would always be zero
    product = 1
    for i in range(0, n, 1):
        product *= (365-i)/365
    return product, 1-product

'''
need to simulate trials and record whether birthdays match or not after randomly assigning numbers 1-365 to the samples
'''

import random
def monte_carlo_simulator(n_trials, n_people):
    n_trials, n_people = int(n_trials), int(n_people)
    outcomes = []
    total_sum = 0
    for i in range (0, n_trials, 1): 
                    
        assignments = []
        for j in range(0, n_people, 1):
            assignments.append(random.randint(1, 365))

        # now need to compare how many people shared a birthday in that sample and probability of sharing as well (maybe need to compare one by one for all)
        count = 0
        for k in range (0, n_people-1, 1):
            for l in range (k+1, n_people, 1):
                if assignments[k] == assignments[l]:
                    count += 1

        if count > 0:
            outcomes.append(int(1))
        else: 
            outcomes.append(int(0))
        
    for i in outcomes:
        total_sum += i

    average_probability = total_sum / n_trials

    return average_probability


print("="*80)
print("For direct computation using closed form: ")
print("="*80)
user_num = input("Enter the number of people: ")
p_no_share, probability_closed = birthday_probability(user_num)

print("The probabilty of two or more people sharing a birthday = ", probability_closed)

print("="*80)
print("For Monte Carlo Simulation: ")
print("="*80)
sample_num = input("Enter the number of people in a room: ")
trials_input = input("Enter the number of rooms: ")
probability= monte_carlo_simulator(trials_input, sample_num)
print(f" The average probabilty for {sample_num} people in {trials_input} rooms is: {probability}")

print("="*100)
print("Now calculating iteratively")
print("="*100)
print("="*80)
print("For direct computation using closed form: ")
print("="*80)
start = input("Enter the starting number of people in a room: ")
end = input("Enter the last number of people in a room: ")
closed_number = []
closed_probability = []
for m in range (int(start), int(end)+1, 1):
    closed_number.append(m)
    closed_probability.append(birthday_probability(m)[1])


print("="*100)
print("Now calculating using monte carlo")
print("="*100)

trials_monte = input("Enter the number of rooms: ")

monte_number = []
monte_probability = []
for n in range (int(start), int(end)+1, 1):
    monte_number.append(n)
    monte_probability.append(monte_carlo_simulator(int(trials_monte), n))



import matplotlib.pyplot as plt

plt.plot(closed_number, closed_probability, label = "Direct computation")
plt.plot(monte_number, monte_probability, label=f"By Monte Carlo Simulation for {trials_monte} simulations")
plt.xlabel("Number of people in a room")
plt.ylabel("Probability of 2 or more people sharing a birthday")
plt.title("Comparing closed form and Monte Carlo Simulation for Birthday Problem")
plt.legend()
plt.tight_layout()
plt.savefig("../results/day02_birthday_problem_comparison.png", dpi=300)
plt.show()

