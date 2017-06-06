# -*- coding: utf-8 -*-
"""
This module contains the fieldtypes.
"""
from mosaicomponents.checkfield import CheckField
from mosaicomponents.colorfield import ColorField
from mosaicomponents.combofield import ComboField
from mosaicomponents.commentfield import CommentField
from mosaicomponents.floatfield import FloatField
from mosaicomponents.iconfield import IconField
from mosaicomponents.intfield import IntField
from mosaicomponents.openfilefield import OpenFileField
from mosaicomponents.savefilefield import SaveFileField
from mosaicomponents.stringfield import StringField

HARPIA_CHECK = "Check"
HARPIA_CODE = "Code"
HARPIA_COLOR = "Color"
HARPIA_COMBO = "Combo"
HARPIA_COMMENT = "Comment"
HARPIA_FLOAT = "Float"
HARPIA_ICON = "Icon"
HARPIA_INT = "Int"
HARPIA_NONE = "None"
HARPIA_OPEN_FILE = "Open File"
HARPIA_SAVE_FILE = "Save File"
HARPIA_STRING = "String"

component_list = {
    HARPIA_CHECK: CheckField,
    HARPIA_COLOR: ColorField,
    HARPIA_COMBO: ComboField,
    HARPIA_COMMENT: CommentField,
    HARPIA_FLOAT: FloatField,
    HARPIA_ICON: IconField,
    HARPIA_INT: IntField,
    HARPIA_OPEN_FILE: OpenFileField,
    HARPIA_SAVE_FILE: SaveFileField,
    HARPIA_STRING: StringField
}
