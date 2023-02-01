from catandmouse import td_qlearning


PATH = 'Example0/trial.csv'


agent = td_qlearning(PATH)

output_q = agent.policy('AC')

print(output_q)