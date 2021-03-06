#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Exp class.
"""
from harpia.GUI.fieldtypes import *
from harpia.model.plugin import Plugin


class Exp(Plugin):
    """
    This class contains methods related the Exp class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)

        # Appearance
        self.help = "Aplica a função exponencial a uma imagem, ou seja, " + \
            "eleva a constante neperiana ao valor " + \
            "de intensidade luminosa de cada ponto da imagem."
        self.label = "Exp"
        self.color = "230:230:60:150"
        self.in_ports = [{"type":"harpia.extensions.c.ports.image",
                          "name":"input_image",
                          "label":"Input Image"}
                         ]
        self.out_ports = [{"type":"harpia.extensions.c.ports.image",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Math Functions"

        # --------------------------C/OpenCv code------------------------------
        self.codes[1] = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes[2] = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_t = cvCreateImage' + \
            '(cvGetSize(block$id$_img_i0), IPL_DEPTH_32F,' + \
            'block$id$_img_i0->nChannels);\n' + \
            'block$id$_img_o0 = cvCloneImage' + \
            '(block$id$_img_i0);\n' + \
            'cvConvertScale(block$id$_img_i0, ' + \
            'block$id$_img_t,(1/255.0),0);\n' + \
            'cvExp(block$id$_img_t, block$id$_img_t);\n' + \
            'cvConvertScale(block$id$_img_t, block$id$_img_o0,' + \
            ' (double)93.8092,0);\n}\n'

        self.codes[3] = \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_t);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
