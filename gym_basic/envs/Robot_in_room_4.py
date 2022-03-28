#https://github.com/MJeremy2017/reinforcement-learning-implementation/blob/master/GridWorld/gridWorld.py
#https://towardsdatascience.com/reinforcement-learning-implement-grid-world-from-scratch-c5963765ebff

# อันนี้ลองตัดให้เหลือให้ ตัวของ ENV เพื่อเอาไปใส่ใน gym แบบ dogtrain
from gym import Env
from gym import spaces
from gym.spaces import Box, Discrete
import random
import numpy as np

'''
# global variables
BOARD_ROWS = 3
BOARD_COLS = 4
WIN_STATE = (0, 3)
LOSE_STATE = (1, 3)
START = (2, 0)
DETERMINISTIC = True
'''

class RobotInRoom(Env):

    def __init__(self):
        self.BOARD_ROWS = 3
        self.BOARD_COLS =4
        self.board = np.zeros([self.BOARD_ROWS, self.BOARD_COLS])   #BOARD_ROWS = 3, BOARD_COLS =4
        self.board[1, 1] = -1  # กำหนด ตำแหน่งที่เป็น หลุมดำ ที่จะลดคะแนน agent
        self.state = [2,0]
        self.isEnd = False
        self.deterministic = True
        self.win_state = [0,3]
        self.lose_state = [1,3]

        self.action_space = spaces.Discrete(4)
        self.collected_reward = 0



    def step(self, action):
        info = {}
        """
                action: up, down, left, right
                -------------
                0 | 1 | 2| 3|
                1 |
                2 |
                return next position
        """

        if action == 0:
            nxtState = [self.state[0] - 1, self.state[1]]
        elif action == 1:
            nxtState = [self.state[0] + 1, self.state[1]]
        elif action == 2:
            nxtState = [self.state[0], self.state[1] - 1]
        else:
            nxtState = [self.state[0], self.state[1] + 1]
        # if next state legal
        if (nxtState[0] >= 0) and (nxtState[0] <= (self.BOARD_ROWS - 1)):
            if (nxtState[1] >= 0) and (nxtState[1] <= (self.BOARD_COLS - 1)):
                if nxtState != [1, 1]:
                    return nxtState

        #giveReward
        if nxtState == self.win_state:
            rw = 1
            self.collected_reward += 1
        elif nxtState == self.lose_state:
            rw = -1
            self.collected_reward += -1
        else:
            rw = -0.04
            self.collected_reward += -0.04

        print("state =", self.state)
        print("action =", action)
        print("next state =", nxtState)
        print("rw =", rw)
        print("sum collected reward =", self.collected_reward)
        print('-----------------')

        self.state = nxtState
        done = bool((self.state == self.win_state )or(self.state == self.lose_state))

        return self.state,self.collected_reward, done, info



    def render(self):
        self.board[self.state] = 1
        for i in range(0, self.BOARD_ROWS):
            print('-----------------')
            out = '| '
            for j in range(0, self.BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')

    def reset(self):
        self.state = [2,0]   # state state
        self.collected_reward = 0
        return self.state, self.collected_reward

