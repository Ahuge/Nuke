from PySide import QtGui, QtCore

# ALPHA_TEXTURE = r"D:\Users\Alex\Pictures\alphaback.png"


class GradientSlider(QtGui.QSlider):
    def __init__(self, min_value, max_value, sensitivity=1000, *args, **kwargs):
        super(GradientSlider, self).__init__(QtCore.Qt.Horizontal, *args, **kwargs)
        self.setStyleSheet("* {color: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"
                       "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 cyan, stop:1 blue);}")
        self.step_size = sensitivity
        self.value_min = min_value
        self.value_max = max_value
        self.setMinimum(0)
        self.setMaximum(self.step_size)

        self._gradient = QtGui.QLinearGradient()
        self._back = QtGui.QBrush()
        # self._back.setTexture(QtGui.QPixmap(ALPHA_TEXTURE))
        self._gradient.setCoordinateMode(self._gradient.StretchToDeviceMode)

    def makeUI(self):
        self.show()
        return self
    def updateValue(self, *args, **kwargs):
        print("UpdateValue!")
        print(args)
        print(kwargs)
        return True

    def value(self):
        range_max = self.value_max - self.value_min
        actual_value = super(GradientSlider, self).value()
        return float(actual_value)/float(self.step_size) * range_max
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        panel = QtGui.QStyleOptionFrame()
        panel.initFrom(self)
        panel.lineWidth = 1
        panel.midLineWidth = 0
        panel.state |= QtGui.QStyle.State_Sunken
        self.style().drawPrimitive(QtGui.QStyle.PE_Frame, panel, painter, self)
        r = self.style().subElementRect(QtGui.QStyle.SE_FrameContents, panel, self)
        painter.setClipRect(r)
        if (self.orientation() == QtCore.Qt.Horizontal):
            self._gradient.setFinalStop(1, 0)
        else:
            self._gradient.setFinalStop(0, 1)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self._back)
        painter.drawRect(self.rect())
        painter.setBrush(self._gradient)
        painter.drawRect(self.rect())
        painter.setClipping(False)

        opt_slider = QtGui.QStyleOptionSlider()
        self.initStyleOption(opt_slider)
        opt_slider.state &= ~QtGui.QStyle.State_HasFocus
        opt_slider.subControls = QtGui.QStyle.SC_SliderHandle
        if self.isSliderDown():
            opt_slider.state |= QtGui.QStyle.State_Sunken
            opt_slider.activeSubControls = QtGui.QStyle.SC_SliderHandle
        #opt_slider.rect = self.style().subControlRect(QtGui.QStyle.CC_Slider, opt_slider, QtGui.QStyle.SC_SliderHandle, self)
        self.style().drawComplexControl(QtGui.QStyle.CC_Slider, opt_slider, painter, self)


def getGradientSlider(minv, maxv, step=1000):
    return nuke.PyCustom_Knob('slider', "werds", "GradientSlider(%f, %f, sensitivity=%s)" % (minv, maxv, step))
knob = getGradientSlider(-25, 50, 100000)
n = nuke.createNode("Grade")
n.addKnob(knob)