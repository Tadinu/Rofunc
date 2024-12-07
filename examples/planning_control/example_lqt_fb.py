"""
LQT feedback version
============================================================

This example shows how a feedback LQT works.
"""
import rofunc as rf
import numpy as np
from rofunc.config.utils import get_config

via_points = np.zeros((3, 7))
via_points[0, :7] = np.array([2, 5, 3, 0, 0, 0, 1])
via_points[1, :7] = np.array([3, 1, 1, 0, 0, 0, 1])
via_points[2, :7] = np.array([5, 4, 1, 0, 0, 0, 1])

cfg = rf.config.utils.get_config("./planning", "lqt")
controller = rf.planning_control.lqt.LQTFb(via_points, cfg)

state_noise = np.vstack((np.array([[3], [-0.5]]), np.zeros((cfg.nbVarX - cfg.nbVar, 1))))
u_hat, x_hat, mu, idx_slices = controller.solve(state_noise)
rf.lqt.plot_3d_uni(x_hat, mu, idx_slices, ori=False, save=False)

