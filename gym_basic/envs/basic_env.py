import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class BasicEnv(gym.Env[np.ndarray, Union[int, np.ndarray]]):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        # There are two actions, first will get reward of 1, second reward of -1. 
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Discrete(2)
        self.state = None

    def step(self, action):

        # if we took an action, we were in state 1
        self.state = 1
    
        if action == 2:
            reward = 1
        else:
            reward = -1
            
        # regardless of the action, game is done after a single step
        done = True

        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.state = 0
        return self.state
  
    def render(self, mode='human'):
        pass

    def close(self):
        pass
