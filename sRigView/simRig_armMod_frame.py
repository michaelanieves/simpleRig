#!/usr/bin/env python
"""
    :module: armModule_frame
    :platform: Maya
    :synopsis: This module calls the neccassary functions to build the arm module frmae callable by a window
    :plans: none
"""
__author__ = "Michael Nieves"
__email__ = "michaelanieves@gmail.com"
__version__ = 1.0

import pymel.core as pm

# UI class
class armModuleFrame(object):
    """ View -- contains arm module frame and corisponding elements
    """
    def __init__(self, inst):
        self.armModuleFrame = pm.frameLayout( parent = inst.simpleSetup_layout, w =244, label='simpleArm', borderStyle='out', cll = True, cl = True )
        self.conTChkBoxGRP = pm.checkBoxGrp( parent = self.armModuleFrame, cw = ( [ 1, 78 ], [ 2, 78 ], [ 3, 78 ] ), numberOfCheckBoxes=3, labelArray3=['Translate X', 'Translate Y', 'Translate Z'], v1 = 1, v2 = 1, v3 =  1 )
        self.conRChkBoxGRP = pm.checkBoxGrp( parent = self.armModuleFrame, cw = ( [ 1, 78 ], [ 2, 78 ], [ 3, 78 ] ),numberOfCheckBoxes=3, labelArray3=['Rotate X', 'Rotate Y', 'Rotate Z'], v1 = 1, v2 = 1, v3 =  1 )
        self.conSChkBoxGRP = pm.checkBoxGrp( parent = self.armModuleFrame, cw = ( [ 1, 78 ], [ 2, 78 ], [ 3, 78 ] ),numberOfCheckBoxes=3, labelArray3=['Scale X', 'Scale Y', 'Scale Z'], v1 = 1, v2 = 1, v3 =  1 )
        self.conVChkBox = pm.checkBox( parent = self.armModuleFrame, label='Visibility', v = 1 )
        self.conTX_Btn = pm.button(parent = self.armModuleFrame, w = 244, h = 24, label="Build simple Arm Module", command = self.build_armMod)
        
    def build_armMod(self, *args):
        print "Yay! You've built an arm module!"
    