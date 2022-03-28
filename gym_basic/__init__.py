from gym.envs.registration import register

register(
    id='basic-v0',
    entry_point='gym_basic.envs:BasicEnv',
)

register(
    id='basic-v2',
    entry_point='gym_basic.envs:BasicEnv2',
)

register(
    id='dog-v0',
    entry_point='gym_basic.envs:DogEnv',
)

register(
    id='robot-v0',
    entry_point='gym_basic.envs:RobotInRoom',
)
