#!/usr/bin/env python
# -*- coding: utf-8 -*-
# noqa: E402
"""
This module contains the BlockManager class.
"""
import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk
from gi.repository import GtkSource
from harpia.GUI.blocknotebook import BlockNotebook
from harpia.GUI.components.codefield import CodeField
from harpia.GUI.components.colorfield import ColorField
from harpia.GUI.components.combofield import ComboField
from harpia.GUI.components.commentfield import CommentField
from harpia.GUI.components.openfilefield import OpenFileField
from harpia.GUI.components.stringfield import StringField
from harpia.GUI.dialog import Dialog
from harpia.GUI.fieldtypes import *
from harpia.GUI.blockporteditor import BlockPortEditor
from harpia.GUI.blockcommoneditor import BlockCommonEditor
from harpia.GUI.blockpropertyeditor import BlockPropertyEditor
from harpia.GUI.blockcodeeditor import BlockCodeEditor
from harpia.model.plugin import Plugin
from harpia.system import System as System
import gettext

_ = gettext.gettext


class BlockEditor(Gtk.Dialog):
    """
    This class contains methods related the BlockManager class
    """

    # ----------------------------------------------------------------------
    def __init__(self, block_manager, block):
        Gtk.Dialog.__init__(self, _("Block Editor"),
                            block_manager,
                            0,
                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        self.block_manager = block_manager
        self.set_default_size(800, 600)
        box = self.get_content_area()

        self.tabs = Gtk.Notebook()
        self.tabs.set_scrollable(True)
        box.pack_start(self.tabs, True, True, 0)

        self.tabs.append_page(BlockCommonEditor(self, block),
                    Gtk.Label(_("Common Properties")))
        self.tabs.append_page(BlockPropertyEditor(self, block),
                    Gtk.Label(_("Properties")))
        self.tabs.append_page(BlockPortEditor(self, block),
                    Gtk.Label(_("Ports")))
        self.tabs.append_page(BlockCodeEditor(self, block),
                    Gtk.Label(_("Code")))

        self.show_all()
        result = self.run()
        if result == Gtk.ResponseType.OK:
            self.block_manager.main_control.add_block(block)
            self.block_manager.update()
        self.close()
        self.destroy()

# ----------------------------------------------------------------------
