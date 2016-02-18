#!/usr/bin/env python
"""
    :module: simpleRig UI
    :platform: Maya
    :synopsis: This module calls the neccassary functions to build the simpleRig UI
    :plans: build the UI with call able functions that can be reorganized at will
"""
__author__ = "Michael Nieves"
__email__ = "michaelanieves@gmail.com"
__version__ = 2.0

# Import functions
import pymel.core as pm
import Color.ColorRange as ColorRange
import simpleRig.sRigView.simRig_armMod_frame as armMod_frame
import simpleRig.sRigView.simRig_initialize_frame as initialize_frame
# reload functions
reload(ColorRange)
reload(initialize_frame)
reload(armMod_frame)

# UI class
class simpleRigUI(object):
    """ View -- contains user interface window and tabs
    """
    def __init__(self):
        title="simpleRig"
        if(pm.windowPref(title, q=True, ex=True)):
            pm.windowPref(title, remove=True)
        if(pm.window(title, q=True, ex=True)):
            pm.deleteUI(title)
            
        # simpleRig window
        self.win = pm.window(title, title="simpleRig v2.0")
        self.winlayout = pm.columnLayout( adj = True )
        self.tabs = pm.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

        # simple setup tab
        self.simpleSetup_layout = pm.columnLayout(parent = self.tabs, adj = True )
        self.simpleSetupText = pm.button( parent = self.simpleSetup_layout, w = 244, h = 24, label = 'simpleSetup' )
        self.simpleSetupToComeText = pm.button( parent = self.simpleSetup_layout, w = 244, h = 24, label = 'simpleSetup Coming Soon!' )
        self.init_frame = initialize_frame.initializeFrame(self)
        self.armMod_frame = armMod_frame.armModuleFrame(self)
        self.simpleSetupbutton_layout = pm.rowColumnLayout(parent = self.simpleSetup_layout, nc = 3 )
        self.sSetup_buildGameRig_button = pm.button( parent = self.simpleSetupbutton_layout, w = 120, h = 24, label = 'Rig 4 Games', c = self.exe_rig4games )
        self.sSetup_buildAnimationRig_button = pm.button( parent = self.simpleSetupbutton_layout, w = 120, h = 24, label = 'Rig 4 Animatinon', c = self.exe_rig4animation )
        self.sSetup_collapseAll_button = pm.button( parent = self.simpleSetupbutton_layout, w = 120, h = 24, label = 'Collapse All', c = self.exe_simpleSetup_collapseAll )
        
        simpleSetup_gradParent=self.simpleSetup_layout
        simpleSetup_color_range = ColorRange.ColorRange([0.0, 0.3, 0.3])
        
        for simpleSetup_grad, color in zip(simpleSetup_gradParent.children(), simpleSetup_color_range.get_range(len(simpleSetup_gradParent.children())) ):
            print simpleSetup_grad, color
            simpleSetup_grad.setBackgroundColor(color)
        
        # simple shapes tab
        self.simpleShapes_layout = pm.columnLayout(parent = self.tabs, adj = True )
        self.simpleShapesText = pm.button( parent = self.simpleShapes_layout, w = 244, h = 24, label = 'simpleShapes' )
        self.simpleShapesToComeText = pm.button( parent = self.simpleShapes_layout, w = 244, h = 24, label = 'simpleShapes Coming Soon!' )
        simpleShapes_gradParent=self.simpleShapes_layout
        
        simpleShapes_color_range = ColorRange.ColorRange([0.0, 0.2, 0.0])
        
        for simpleShapes_grad, color in zip(simpleShapes_gradParent.children(), simpleShapes_color_range.get_range(len(simpleShapes_gradParent.children())) ):
            print simpleShapes_grad, color
            simpleShapes_grad.setBackgroundColor(color)
            
        # simple curves tab
        self.simpleCurves_layout = pm.columnLayout(parent = self.tabs, adj = True )
        self.simpleCurvesText = pm.button( parent = self.simpleCurves_layout, w = 244, h = 24, label = 'simpleCurves' )
        self.simpleCurvesToComeText = pm.button( parent = self.simpleCurves_layout, w = 244, h = 24, label = 'simpleCurves Coming Soon!' )
        simpleCurves_gradParent=self.simpleCurves_layout
        
        simpleCurves_color_range = ColorRange.ColorRange([0.0, 0.2, 0.0])
        
        for simpleCurves_grad, color in zip(simpleCurves_gradParent.children(), simpleCurves_color_range.get_range(len(simpleCurves_gradParent.children())) ):
            print simpleCurves_grad, color
            simpleCurves_grad.setBackgroundColor(color)
        
        # Edit Tab Layout labels
        pm.tabLayout( self.tabs, edit=True, tabLabel=( (self.simpleSetup_layout, 'simpleSetup'), (self.simpleShapes_layout, 'simpleShapes'), ( self.simpleCurves_layout, 'simpleCurves') ) )
        
        # Window Functions
        self.closeTool_Btn = pm.button(parent = self.winlayout,w = 330, h = 24, label="Close Tool", command = self.exitWin)
        self.delete = []
        self.win.show()

    # window functions
    def exe_rig4games(self, *args, **kwargs):
        """ This function contains the nessacery commands to execute a simpleRig game ready Rig
        Args:
            None
        Returns (None)
        """
        print 'Yay! your game rig is ready!' 
        
    def exe_rig4animation(self, *args, **kwargs):
        """ This function contains the nessacery commands to create a simpleRig animation ready Rig
        Args:
            None
        Returns (None)
        """
        print 'Yay! your animation rig is ready!' 
        
    def exe_simpleSetup_collapseAll(self, *args, **kwargs):
        """ This function contains the nessacery commands to create a simpleRig animation ready Rig
        Args:
            None
        Returns (None)
        """
        print 'Yay! you collapsed the simple setup frames!' 
        
    def exitWin(self, *args, **kwargs):
        """ This function can Close the UI
        Args:
            None
        Returns (None)
        """
        if kwargs.get('debug'):
            print "NO STOP IT!!!"
        pm.deleteUI(self.win)

# Open UI        
if __name__ == '__main__':
    my_ui = simpleRigUI()
    