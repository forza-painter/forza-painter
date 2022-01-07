# Discord: A-Dawg#0001 (AE)
# Supports: Forza Horizon 5
# Offically: MS Store/XBOX PC App (latest version), Steam (latest version).
# Unofficially: Every version that isn't running on a console of via cloud gaming should work.
# License: MIT
# Year: 2022

import struct

class Color:
    r: int
    g: int
    b: int
    a: int
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    def get_struct(self):
        return (  struct.pack('B', self.r)
                + struct.pack('B', self.g)
                + struct.pack('B', self.b)
                + struct.pack('B', self.a))

class Shape:
    type_id: int
    x: int
    y: int
    w: int
    h: int
    rot_deg: int
    color: Color
    is_mask: bool
    def __init__(self, type_id, x, y, w, h, rot_deg, color: Color, is_mask):
        self.type_id = type_id
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rot_deg = rot_deg
        self.color = color
        self.is_mask = is_mask