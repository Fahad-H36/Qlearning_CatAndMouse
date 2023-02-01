import pandas as pd

class td_qlearning:

  qTable = {}


  def __init__(self, trial_filepath):

    # trial_filepath is the path to a file containing a trial through state space
    # Implementation of qLearning
    # Return nothing
    self.table = pd.read_csv(trial_filepath)
    self.keys = list(self.table[self.table.columns[0]])
    self.keys.insert(0, self.table.columns[0])

    self.values = list(self.table[self.table.columns[1]])
    self.values.insert(0, self.table.columns[1])


    self.alpha = 0.05
    self.gamma=0.95
    self.qTable = dict(zip(list(set(self.keys)), [None]*len(list(set(self.keys)))))

    for i in self.qTable:
      self.qTable[i] = {}


    for i in range(len(self.keys)):

      state = self.keys[i]
      action = self.values[i]


      if state[0] == state[1]:
        reward = -10
      elif state[0] == 'B':
        reward = -1
      else:
        reward = 1

      temp = self.qTable[state]

 

      if action not in temp.keys():
        current_q = 0
      else:
        current_q = temp[action]




      if i < len(self.keys)-1:
        nextState = self.keys[i+1]

        if len(self.qTable[nextState]) > 0:
          future_q = max(self.qTable[nextState].values())
        else:
          future_q = 0

      else:
        future_q = 0




      temp[action] = current_q + self.alpha*(reward+self.gamma*future_q - current_q)

      self.qTable[state] = temp
    




  def qvalue(self, state, action):
    # getter method
    # state is a string representation of a state
    # action is a string representation of an action
    # Return the q-value for the state-action pair

      if state in self.qTable and action in self.qTable[state]:
        q = round(self.qTable[state][action], 2)
      else:
        q = 0
      return q

 
  def policy(self, state):
    # getter Method
    # state is a string representation of a state
    # Return the optimal action under the learned policy

    if state in self.qTable:
      a = max(self.qTable[state], key = self.qTable[state].get)
    else:
      a = 'N'
    return a

