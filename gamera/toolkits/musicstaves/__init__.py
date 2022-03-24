"""
Toolkit setup

This file is run on importing anything within this directory.
Its purpose is only to help with the Gamera GUI shell,
and may be omitted if you are not concerned with that.
"""

from gamera import toolkit
import wx
#import plugins
#from gamera.toolkits.musicstaves import main

#from gamera.toolkits.musicstaves.plugins import vector_field

# You can inherit from toolkit.CustomMenu to create a menu
# for your toolkit.  Create a list of menu option in the
# member _items, and a series of callback functions that
# correspond to them.  The name of the callback function
# should be the same as the menu item, prefixed by '_On'
# and with all spaces converted to underscores.
class MusicstaveMenu(toolkit.CustomMenu):
    _items = ["Musicstave Toolkit"]
    def _OnMusicstave_Toolkit(self, event):
        wx.MessageDialog(None, "You clicked on Musicstave Toolkit!").ShowModal()
        main.main()
musicstave_menu = MusicstaveMenu()
