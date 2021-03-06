#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.3 on Mon Feb  3 00:13:53 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Settings(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Settings.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW | wx.STAY_ON_TOP
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((412, 183))
        self.radio_units = wx.RadioBox(self, wx.ID_ANY, "Units", choices=["mm", "cm", "inch", "mils"], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.combo_language = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.check_list_box_1 = wx.CheckListBox(self, wx.ID_ANY, choices=["Invert Mouse Wheel Zoom", "Autoclose Shutdown"])

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.on_radio_units, self.radio_units)
        self.Bind(wx.EVT_COMBOBOX, self.on_combo_language, self.combo_language)
        self.Bind(wx.EVT_CHECKLISTBOX, self.on_checklist_settings, self.check_list_box_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Settings.__set_properties
        self.SetTitle("Settings")
        self.radio_units.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.radio_units.SetToolTip("Set default units for guides")
        self.radio_units.SetSelection(0)
        self.combo_language.SetToolTip("Select the desired language to use.")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Settings.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Language"), wx.HORIZONTAL)
        sizer_5.Add(self.radio_units, 0, wx.EXPAND, 0)
        sizer_2.Add(self.combo_language, 0, 0, 0)
        sizer_5.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.check_list_box_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_6, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_radio_units(self, event):  # wxGlade: Settings.<event_handler>
        print("Event handler 'on_radio_units' not implemented!")
        event.Skip()

    def on_combo_language(self, event):  # wxGlade: Settings.<event_handler>
        print("Event handler 'on_combo_language' not implemented!")
        event.Skip()

    def on_checklist_settings(self, event):  # wxGlade: Settings.<event_handler>
        print("Event handler 'on_checklist_settings' not implemented!")
        event.Skip()

# end of class Settings

class MyApp(wx.App):
    def OnInit(self):
        self.Settings = Settings(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Settings)
        self.Settings.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
