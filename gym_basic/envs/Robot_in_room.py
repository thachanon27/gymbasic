#modify from
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
        self.boardpenalty = -1  # กำหนด ตำแหน่งที่เป็น หลุมดำ ที่จะลดคะแนน agent ที่ตำแหน่ง [1,1]
        self.state_x = 2
        self.state_y = 0
        #self.state = [2,0]
        self.isEnd = False
        self.deterministic = True
        self.win_state = [0, 3]
        self.win_state_x = 0    # self.win_state_x = [0,3]
        self.win_state_y = 3
        self.lose_state = [1, 3]
        self.lose_state_x = 1  #self.lose_state = [1,3]
        self.lose_state_y = 3

        self.action_space = spaces.Discrete(4)
        self.collected_reward = 0
        # no. of rounds
        self.rounds = 0

    def step(self, action):
        info = {}
        move_x = 0
        move_y = 0
        self.rounds += 1
        """
                action: up, down, left, right
                -------------
                0 | 1 | 2| 3|
                1 |
                2 |
                return next position
        """
        nxtState2_x, nxtState2_y  = self.state

        if action == 0:
            move_x = -1
            move_y = 0
        elif action == 1:
            move_x =  1
            move_y = 0
        elif action == 2:
            move_x = 0
            move_y = -1
        elif action == 3:
            move_x = 0
            move_y = 1

        nxtState_x, nxtState_y = self.state
        print("round =", self.rounds)
        #print("state =", self.state)
        nxtState_x += move_x
        nxtState_y += move_y
        #print("action =", action)
        #print("next state x =", nxtState_x, ",next state y =", nxtState_y)

        # if next state legal
        if (nxtState_x >= 0) and (nxtState_x <= 2) :
            #print("1")
            if (nxtState_y >= 0) and (nxtState_y <= 3):
                #print("2")
                #if (nxtState_x !=1  and  not nxtState_y != 1:   # บรรทัดนี้ ทำยังไงก็ไม่ได้เงื่อนไข ที่ห้าม x,y = 1,1 เลยข้ามไปก่อน
                #print("3")
                nxtState2_x = nxtState_x
                nxtState2_y = nxtState_y
                    #return nxtState
        #nxtState = nxtPosition(self, action)
        #giveReward

        #nxtState2_x = nxtState_x
        #nxtState2_y = nxtState_y

        if nxtState2_x == self.win_state_x and nxtState2_y == self.win_state_y:
            rw = 1
            self.collected_reward += 1
        elif nxtState2_x == self.lose_state_x and nxtState2_y == self.lose_state_y:
            rw = -1
            self.collected_reward += -1
        else:
            rw = -0.04
            self.collected_reward += -0.04

        #print("state =", self.state)
        #print("action =", action)
        #print("next state x2 =", nxtState2_x,",next state y2 =", nxtState2_y  )
        #print("rw =", rw)
        print("sum collected reward =", self.collected_reward)
        if rw == 1: 
            print("found win state") 
        if rw == -1: 
            print("fail at lose state") 
        print('-----------------')

        self.state = (nxtState2_x, nxtState2_y)
        done = bool((nxtState2_x == self.win_state_x and nxtState2_y == self.win_state_y  )
                    or(nxtState2_x == self.lose_state_x and nxtState2_y == self.lose_state_y ))

        return np.array(self.state, dtype=np.float32),self.collected_reward, done, info



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

'''
env = RobotInRoom()
state = env.reset()
done = False
while not done:
    #state = env.reset()
    action = env.action_space.sample()
    #print("action = ", action)
    state, reward, done, info = env.step(action)
'''

'''
    def nxtPosition(self, action):
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
        return self.state
'''
