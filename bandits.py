# Making some bandits! 
import numpy as np
import matplotlib.pyplot as plt
import random 
random.seed(42)

# Following simple bandit algorithm 

class Testbed():
    def __init__(self, num_bandits):
        self.num_bandits = num_bandits 

    def action_values(self):
        q_vals = np.random.randn(self.num_bandits)
        return q_vals

class Bandits():
    def __init__(self, epsilon): 
        self.epsilon = epsilon 

        def simple_bandit(): 
            return 

        def learn():
            return 

    

epsilon = 0.1 
bandits = 10
testbed = Testbed(bandits)
q_star = testbed.action_values()
actions = range(1, bandits+1)
fig, ax = plt.subplots()
ax.scatter(actions, q_star, )
for i, txt in enumerate(actions):
    ax.annotate(txt, (actions[i], q_star[i]))
plt.show()

if __name__ == '__main__':
    # do something
    print("hi")
