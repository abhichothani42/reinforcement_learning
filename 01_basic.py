import gymnasium as gym

env = gym.make("Pendulum-v1", render_mode="human")
state, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # agent policy that uses the observation and info
    state, reward, terminated, truncated, info = env.step(action)

    episode_over = terminated or truncated

env.close()