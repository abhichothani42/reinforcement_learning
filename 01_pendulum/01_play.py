### run as sudo because using keyboard lib
import gymnasium as gym
import keyboard
import numpy as np

def get_action_from_keyboard():
    torque = 0.0
    applied_torque = 1

    if keyboard.is_pressed('left'):
        torque = -applied_torque
    elif keyboard.is_pressed('right'):
        torque = applied_torque
    
    return np.array([torque], dtype=np.float32)

def play():
    env = gym.make("Pendulum-v1", render_mode="human")

    state, info = env.reset()
    total_reward = 0

    print("--- Pendulum Game ---")
    print("Use LEFT arrow key for negative torque (counter-clockwise).")
    print("Use RIGHT arrow key for positive torque (clockwise).")
    print("If no key is pressed, torque will be zero.")
    print("Press 'q' to quit.")
    print("Goal: Swing up and balance the pendulum at the top (angle 0).")

    try:
        while True:
            env.render()

            #get action from keyboard
            action = get_action_from_keyboard()

            #Take a step in the env
            state, reward, done, truncated, info = env.step(action)

            total_reward += reward

            #check for quit key
            if keyboard.is_pressed('q'):
                print("quitting the game.")
                break
    
    except KeyboardInterrupt:
        print("\nGame interrupted.")

    finally:
        env.close()
        print(f"Game Over! Total Reward: {total_reward:.2f}")

if __name__=='__main__':
    play()