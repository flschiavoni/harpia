# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
"""
This module contains the BlockControl class.
"""
import ast
import os
import inspect  # For module inspect
import pkgutil  # For dynamic package load
from os.path import expanduser
from harpia.utils.XMLUtils import XMLParser
from harpia.utils.PythonUtils import PythonParser
from harpia.model.plugin import Plugin
from harpia.persistence.blockpersistence import BlockPersistence

class BlockControl():
    """
    This class contains methods related the BlockControl class.
    """

    # ----------------------------------------------------------------------

    def __init__(self):
        pass

    # ----------------------------------------------------------------------
    @classmethod
    def export_xml(cls):
        from harpia.system import System as System
        System()
        for block in System.blocks:
            print "Exporting block " + block
            BlockPersistence.save(System.blocks[block])

    # ----------------------------------------------------------------------
    @classmethod
    def export_python(cls):
        from harpia.system import System as System
        System()
        for block in System.blocks:
            print "Exporting block " + block
            BlockPersistence.save_python(System.blocks[block])

    # ----------------------------------------------------------------------
    @classmethod
    def load(cls, file_name):
        """
        This method loads the block from XML file.

        Returns:

            * **Types** (:class:`boolean<boolean>`)
        """
        BlockPersistence.load(file_name)
    # ----------------------------------------------------------------------
    @classmethod
    def add_block(cls, block):
        # first, save it
        BlockPersistence.save(block)
        # Then add it to system
        from harpia.system import System
        System.blocks[block.type] = block

    # ----------------------------------------------------------------------
    @classmethod
    def delete_block(cls, block):
        from harpia.system import System
        if block.source == "xml":
            data_dir = System.get_user_dir() + "/extensions/"
            file_name = data_dir + block.type + ".xml"
            os.remove(file_name)
            System.blocks.pop(block.type, None)
            return True
        else:
            return False

    # ----------------------------------------------------------------------
    @classmethod
    def print_block(cls, block):
        """
        This method prints the block properties.
        """
        print 'Block.id =', block.id
        print 'Block.x =', block.x
        print 'Block.y =', block.y

        print 'Block.type =', block.type
        print 'Block.language =', block.language
        print 'Block.framework =', block.framework
        print 'Block.source =', block.source

        # Appearance
        print 'Block.help =', block.help
        print 'Block.label =', block.label
        print 'Block.color =', block.color
        print 'Block.group =', block.group
        print 'Block.in_ports =', block.in_ports
        print 'Block.out_ports =', block.out_ports

        # Code generation
        print 'Block.properties =', block.properties
        print 'Block.codes =', block.codes
# ----------------------------------------------------------------------
