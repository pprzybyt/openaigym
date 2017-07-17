import gym
import sys
import time
from matplotlib import pyplot as plt

NAME = "Pong-v0"
SNAPSHOTS = "snapshots/"

try:
    env = gym.make(NAME)
    env.reset()
    counter = 0


    while 1:
        counter += 1
        if counter % 100 == 0:
            plt.imshow(env.render('rgb_array'))
            plt.savefig(SNAPSHOTS + str(counter) + ".png")
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        #print counter, ": ", observation

        if done:
            sys.exit()
        env.render()
        time.sleep(0.01)

except IndexError:
    sys.exit()
except KeyboardInterrupt:
    sys.exit()


