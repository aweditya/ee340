#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class happy_birthday(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "happy_birthday")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_float*1, (16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000, 16000))
        self.audio_sink_0 = audio.sink(samp_rate, '', False)
        self.analog_sig_source_x_0_0_0_0_0_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 466.16, 1, 0, 0)
        self.analog_sig_source_x_0_0_0_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 440, 1, 0, 0)
        self.analog_sig_source_x_0_0_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 523.25, 1, 0, 0)
        self.analog_sig_source_x_0_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 392, 1, 0, 0)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 329.63, 1, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 349.23, 1, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 293.66, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 262, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 13))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 12))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 9))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 7))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 6))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_stream_mux_0, 3))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_stream_mux_0, 2))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_stream_mux_0, 8))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_stream_mux_0, 4))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_stream_mux_0, 22))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_stream_mux_0, 24))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_stream_mux_0, 17))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_stream_mux_0, 11))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_stream_mux_0, 18))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.blocks_stream_mux_0, 5))
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 10))
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 23))
        self.connect((self.analog_sig_source_x_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 16))
        self.connect((self.analog_sig_source_x_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 14))
        self.connect((self.analog_sig_source_x_0_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 21))
        self.connect((self.analog_sig_source_x_0_0_0_0_0_0_0, 0), (self.blocks_stream_mux_0, 15))
        self.connect((self.analog_sig_source_x_0_0_0_0_0_0_1, 0), (self.blocks_stream_mux_0, 19))
        self.connect((self.analog_sig_source_x_0_0_0_0_0_0_1, 0), (self.blocks_stream_mux_0, 20))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.audio_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "happy_birthday")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0_0_0_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)




def main(top_block_cls=happy_birthday, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
