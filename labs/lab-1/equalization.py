#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: aditya
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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class equalization(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "equalization")

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
        self.samp_rate = samp_rate = 48000
        self.band5_9000_15000 = band5_9000_15000 = 1
        self.band4_6000_9000 = band4_6000_9000 = 1
        self.band3_3000_6000 = band3_3000_6000 = 1
        self.band2_500_3000 = band2_500_3000 = 1
        self.band1_20_500 = band1_20_500 = 1

        ##################################################
        # Blocks
        ##################################################
        self._band5_9000_15000_range = Range(1, 10, 1, 1, 200)
        self._band5_9000_15000_win = RangeWidget(self._band5_9000_15000_range, self.set_band5_9000_15000, "'band5_9000_15000'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band5_9000_15000_win)
        self._band4_6000_9000_range = Range(1, 10, 1, 1, 200)
        self._band4_6000_9000_win = RangeWidget(self._band4_6000_9000_range, self.set_band4_6000_9000, "'band4_6000_9000'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band4_6000_9000_win)
        self._band3_3000_6000_range = Range(1, 10, 1, 1, 200)
        self._band3_3000_6000_win = RangeWidget(self._band3_3000_6000_range, self.set_band3_3000_6000, "'band3_3000_6000'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band3_3000_6000_win)
        self._band2_500_3000_range = Range(1, 10, 1, 1, 200)
        self._band2_500_3000_win = RangeWidget(self._band2_500_3000_range, self.set_band2_500_3000, "'band2_500_3000'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band2_500_3000_win)
        self._band1_20_500_range = Range(1, 10, 1, 1, 200)
        self._band1_20_500_win = RangeWidget(self._band1_20_500_range, self.set_band1_20_500, "'band1_20_500'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._band1_20_500_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/aditya/Projects/iitb/ee340/labs/audio/Bach.wav', True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band2_500_3000,
                samp_rate,
                500,
                3000,
                10,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band5_9000_15000,
                samp_rate,
                9000,
                15000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band4_6000_9000,
                samp_rate,
                6000,
                9000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band3_3000_6000,
                samp_rate,
                3000,
                6000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                band1_20_500,
                samp_rate,
                20,
                500,
                10,
                window.WIN_HAMMING,
                6.76))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.band_pass_filter_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.band_pass_filter_0_0_1, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "equalization")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.band1_20_500, self.samp_rate, 20, 500, 10, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.band3_3000_6000, self.samp_rate, 3000, 6000, 100, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(self.band4_6000_9000, self.samp_rate, 6000, 9000, 100, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0_1.set_taps(firdes.band_pass(self.band5_9000_15000, self.samp_rate, 9000, 15000, 100, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.band2_500_3000, self.samp_rate, 500, 3000, 10, window.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_band5_9000_15000(self):
        return self.band5_9000_15000

    def set_band5_9000_15000(self, band5_9000_15000):
        self.band5_9000_15000 = band5_9000_15000
        self.band_pass_filter_0_0_1.set_taps(firdes.band_pass(self.band5_9000_15000, self.samp_rate, 9000, 15000, 100, window.WIN_HAMMING, 6.76))

    def get_band4_6000_9000(self):
        return self.band4_6000_9000

    def set_band4_6000_9000(self, band4_6000_9000):
        self.band4_6000_9000 = band4_6000_9000
        self.band_pass_filter_0_0_0.set_taps(firdes.band_pass(self.band4_6000_9000, self.samp_rate, 6000, 9000, 100, window.WIN_HAMMING, 6.76))

    def get_band3_3000_6000(self):
        return self.band3_3000_6000

    def set_band3_3000_6000(self, band3_3000_6000):
        self.band3_3000_6000 = band3_3000_6000
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.band3_3000_6000, self.samp_rate, 3000, 6000, 100, window.WIN_HAMMING, 6.76))

    def get_band2_500_3000(self):
        return self.band2_500_3000

    def set_band2_500_3000(self, band2_500_3000):
        self.band2_500_3000 = band2_500_3000
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.band2_500_3000, self.samp_rate, 500, 3000, 10, window.WIN_HAMMING, 6.76))

    def get_band1_20_500(self):
        return self.band1_20_500

    def set_band1_20_500(self, band1_20_500):
        self.band1_20_500 = band1_20_500
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.band1_20_500, self.samp_rate, 20, 500, 10, window.WIN_HAMMING, 6.76))




def main(top_block_cls=equalization, options=None):

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
