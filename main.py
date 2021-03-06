# --------------------------------------------------------
# Particle Filter
# Licensed under The MIT License
# Written by Ye Liu (ye-liu at whu.edu.cn)
# --------------------------------------------------------

from math import cos, sin

import numpy as np

from particle_filter import ParticleFilter
from utils import get_default_hyperparams, plot


def create_curve(n, d, r):
    pts = []
    cur_r = r
    for i in range(n):
        for a in range(1, 360, 4):
            r = cur_r + d * a / 360.0
            a *= np.pi / 180.0
            pts.append((r * cos(a), r * sin(a)))
        cur_r += d
    return pts


def main():
    hyperparams = get_default_hyperparams()
    pf = ParticleFilter(**hyperparams)

    pts = create_curve(2, 15, 0)
    for pt in pts:
        predict_pts = pf.update_state(pt)

    plot(pf.actual_pts, pf.estimate_pts, predict_pts, pf.particles)


if __name__ == '__main__':
    main()
