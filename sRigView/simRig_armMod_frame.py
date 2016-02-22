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
        self.armSide_RBGRP = pm.radioButtonGrp( label='Choose Arm Side', labelArray3=['Left', 'Center', 'Right'], numberOfRadioButtons=3 )
        self.armSpace_RBGRP = pm.radioButtonGrp( label='Choose Arm Space', labelArray3=['Top', 'Middle', 'Bottom'], numberOfRadioButtons=3 )
        self.armAttribute_ChkBoxGRP = pm.checkBoxGrp( parent = self.armModuleFrame, label = 'Arm Attributes   ', cw = ( [ 1, 90 ], [ 2, 70 ], [ 3, 100 ], [ 4, 60 ] ),numberOfCheckBoxes=3, labelArray3=['Stretchy', 'Elbow Pinning', 'Bendy Arms'], v1 = 1, v2 = 1, v3 =  1 )
        
        self.armModulebutton_layout = pm.rowColumnLayout(parent = self.armModuleFrame, nc = 3 )
        self.buildArm_Btn = pm.button(parent = self.armModulebutton_layout, w = 120, h = 24, label="Build Arm", command = self.build_armMod)
        self.mirrorArm_Btn = pm.button( parent = self.armModulebutton_layout, w = 120, h = 24, label = 'Mirror Arm', c = self.exe_MirrorArm )
        self.collapseArmModule_Btn = pm.button( parent = self.armModulebutton_layout, w = 120, h = 24, label = 'Collapse Arm Module', c = self.exe_collapseArmModule )
        
    def build_armMod(self, *args):
        print "Yay! You've built an arm module!"

    def exe_MirrorArm(self, *args):
        print "Yay! You've mirrored the arm module!"  
        
    def exe_collapseArmModule(self, *args):
        print "Yay! You've collapsed the arm module!" 