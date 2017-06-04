#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Circle class.
"""
from harpia.GUI.fieldtypes import *
from harpia.model.plugin import Plugin


class Circle(Plugin):
    """
    This class contains methods related the Circle class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        Plugin.__init__(self)
        self.x0 = 100
        self.y0 = 100
        self.circle_color = "#0000ffff0000"
        self.language = "c"
        self.framework = "opencv"

        self.red = self.circle_color[1:5]
        self.green = self.circle_color[5:9]
        self.blue = self.circle_color[9:13]

        self.red = int(self.red, 16) / 257
        self.green = int(self.green, 16) / 257
        self.blue = int(self.blue, 16) / 257

        # Appearance
        self.help = "Desenha Circulos."
        self.label = "Circle"
        self.color = "255:0:0:150"
        self.in_types = ["harpia.extensions.c.ports.image", "harpia.extensions.c.ports.int", "harpia.extensions.c.ports.int"]
        self.out_types = ["harpia.extensions.c.ports.image"]
        self.group = "Basic Shapes"

        self.properties = [{"name": "x0",
                            "label": "x0",
                            "type": HARPIA_INT,
                            "lower": 0,
                            "upper": 800,
                            "step": 1
                            },
                           {"name": "y0",
                            "label": "y0",
                            "type": HARPIA_INT,
                            "lower": 0,
                            "upper": 1000,
                            "step": 1
                            },
                           {"name": "Color",
                            "label": "circle_color",
                            "type": HARPIA_COLOR
                            }
                           ]

        # -----------------C/OpenCv code ---------------------------
        self.codes[1] = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'int block$id$_int_i1 = $x0$;\n' + \
            'int block$id$_int_i2 = $y0$;\n'

    # ----------------------------------------------------------------------
    def generate_vars(self):
        self.x0 = int(self.x0)
        self.y0 = int(self.y0)

        return self.codes[1]

    # ----------------------------------------------------------------------
    def generate_function_call(self):
        self.red = self.circle_color[1:5]
        self.green = self.circle_color[5:9]
        self.blue = self.circle_color[9:13]

        self.red = int(self.red, 16) / 257
        self.green = int(self.green, 16) / 257
        self.blue = int(self.blue, 16) / 257
        return \
            '\nif(block$id$_img_i0){\n' + \
            'CvPoint center = cvPoint' + \
            '(block$id$_int_i1, block$id$_int_i2);\n' + \
            'CvScalar color = cvScalar($blue$,$green$,$red$,0);\n' + \
            'cvCircle(block$id$_img_i0, center, 10, color, 1, 8, 0);\n' +\
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            '}\n'
# -----------------------------------------------------------------------------
