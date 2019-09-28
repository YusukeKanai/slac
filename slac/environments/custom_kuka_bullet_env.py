"""
__author__ = "Yusuke Kanai"
__copyright__ = "Copyright (C) 2018 Yusuke Kanai"
__licence__ = "MIT"
__version = "0.1"
"""

# -*- coding:utf-8 -*-

from __future__ import print_function, unicode_literals, division

from pybullet_envs.bullet.kukaGymEnv import KukaGymEnv
import pybullet_envs.bullet.kukaGymEnv as kukaEnv
from gym.envs.registration import register
import gym


class CustomKukaBulletEnv(KukaGymEnv):
    def __init__(self):
        KukaGymEnv.__init__(self)
        self._cam_yaw = 70.
        self._cam_pitch = -30.
        self._cam_dist = 1.8

    def set_render_size(self, height, width):
        kukaEnv.RENDER_HEIGHT = height
        kukaEnv.RENDER_WIDTH = width

    def get_time_step(self):
        return self._timeStep


def register_environment():
    register(
        id="CustomKukaButtetEnv-v0",
        entry_point="slac.environments.custom_kuka_bullet_env:CustomKukaBulletEnv",
        max_episode_steps=1000,
        reward_threshold=5.0
    )


if __name__ == '__main__':
    register_environment()
    env = gym.make("CustomKukaButtetEnv-v0")
    env.reset()
    env.render()
    env.get_time_step()
    a = env.action_space.sample()
    env.step(a)
