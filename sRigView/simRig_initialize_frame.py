#!/usr/bin/env python
"""
    :module: initialize_frame
    :platform: Maya
    :synopsis: This module calls the neccassary functions to build the initialize frmae callable by a window
    :plans: none
"""
__author__ = "Michael Nieves"
__email__ = "michaelanieves@gmail.com"
__version__ = 1.0

import pymel.core as pm

# UI class
class initializeFrame(object):
    """ View -- contains initialize frame and corisponding elements
    """
    def __init__(self, inst):
        self.initializeFrame = pm.frameLayout( parent = inst.simpleSetup_layout, w =244, label='Initialize', borderStyle='out', cll = True, cl = True )
        self.nameRigTFBG = pm.textFieldButtonGrp( parent = self.initializeFrame, cw = ( [ 1, 110 ],  [ 2, 210 ], [ 3, 40 ] ), cal = ( 2, 'center'), label='Rig Name   ', pht='              >>> Name Your Rig <<<', buttonLabel='Load', cc = self.rigName_load, bc = self.rigName_load )
        self.displayVisChkBoxGRP = pm.checkBoxGrp( parent = self.initializeFrame, label = 'Display Visibility   ', cw = ( [ 1, 110 ], [ 2, 80 ], [ 3, 80 ], [ 4, 80 ]  ), numberOfCheckBoxes = 3, labelArray3 = ['Model', 'Skeleton', 'Control'], v1 = 1, v2 = 1, v3 =  1 )
        self.displayTypeChkBoxGRP = pm.checkBoxGrp( parent = self.initializeFrame, label = 'Display Type   ', cw = ( [ 1, 110 ], [ 2, 80 ], [ 3, 80 ], [ 4, 80 ]  ), numberOfCheckBoxes = 3, labelArray3 = ['Model', 'Skeleton', 'Control'], v1 = 1, v2 = 1, v3 =  1 )
        self.additionalAttrsChkBoxGRP = pm.checkBoxGrp( parent = self.initializeFrame, label = 'Additional Attributes   ', cw = ( [ 1, 110 ], [ 2, 80 ], [ 3, 80 ], [ 4, 80 ]  ), numberOfCheckBoxes = 3, labelArray3 = ['Speed', 'Pose', 'Costume'] )
        
    def rigName_load(self, *args):
        print "yay you've loaded your rigs name!"