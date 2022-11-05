#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.9.8.0-rc1

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
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class endsem(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "endsem")

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
        self.symb_rate = symb_rate = 10000
        self.sps = sps = 4
        self.samp_rate = samp_rate = sps*symb_rate
        self.quad_rate = quad_rate = 2000000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=int(quad_rate/samp_rate),
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=int(quad_rate/samp_rate),
                taps=[],
                fractional_bw=0)
        self.low_pass_filter_0_0_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                10000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                quad_rate,
                70000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                quad_rate,
                70000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.iir_filter_xxx_0 = filter.iir_filter_ccf([1], [1,0,0,0,-0.5], True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_fff(sps, 2*3.14159/100, firdes.root_raised_cosine(32, 32*samp_rate, symb_rate, 0.4, 1408), 32, 16, 1.5, 1)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-50e-6, 50e-6, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 7)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/aditya/Projects/iitb/ee340/exams/endsem/rx.dat', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/aditya/Projects/iitb/ee340/exams/endsem/out.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(quad_rate, analog.GR_SIN_WAVE, 500000, 2, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(quad_rate, analog.GR_COS_WAVE, 500000, -2, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.blocks_float_to_complex_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "endsem")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samp_rate(self.sps*self.symb_rate)
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(32, 32*self.samp_rate, self.symb_rate, 0.4, 1408))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_samp_rate(self.sps*self.symb_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(32, 32*self.samp_rate, self.symb_rate, 0.4, 1408))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 10000, 1000, window.WIN_HAMMING, 6.76))

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.quad_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.quad_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.quad_rate, 70000, 10000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.quad_rate, 70000, 10000, window.WIN_HAMMING, 6.76))




def main(top_block_cls=endsem, options=None):

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
