import gym 

env = gym.make('CartPole-v1',render_mode='human')

env.reset()
for _ in range(100):
    env.render()

    accion= env.action_space.sample()
    env.step(accion)

env.close()