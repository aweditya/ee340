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

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class end_to_end(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "end_to_end")

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
        self.sps = sps = 10
        self.samp_rate = samp_rate = symb_rate*sps
        self.tx_taps = tx_taps = firdes.root_raised_cosine(40, samp_rate, symb_rate, 0.99, 11*sps*32)
        self.rx_taps = rx_taps = firdes.root_raised_cosine(40, 32*samp_rate, symb_rate, 0.99, 11*sps*32)
        self.quad_rate = quad_rate = 5*samp_rate
        self.noise = noise = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._noise_range = Range(0, 1, 0.001, 0.5, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "'noise'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_win)
        self.constellations = Qt.QTabWidget()
        self.constellations_widget_0 = Qt.QWidget()
        self.constellations_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellations_widget_0)
        self.constellations_grid_layout_0 = Qt.QGridLayout()
        self.constellations_layout_0.addLayout(self.constellations_grid_layout_0)
        self.constellations.addTab(self.constellations_widget_0, 'Before Transmission')
        self.constellations_widget_1 = Qt.QWidget()
        self.constellations_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellations_widget_1)
        self.constellations_grid_layout_1 = Qt.QGridLayout()
        self.constellations_layout_1.addLayout(self.constellations_grid_layout_1)
        self.constellations.addTab(self.constellations_widget_1, 'After CMA Equalization')
        self.constellations_widget_2 = Qt.QWidget()
        self.constellations_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellations_widget_2)
        self.constellations_grid_layout_2 = Qt.QGridLayout()
        self.constellations_layout_2.addLayout(self.constellations_grid_layout_2)
        self.constellations.addTab(self.constellations_widget_2, 'After Costas Loop')
        self.constellations_widget_3 = Qt.QWidget()
        self.constellations_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.constellations_widget_3)
        self.constellations_grid_layout_3 = Qt.QGridLayout()
        self.constellations_layout_3.addLayout(self.constellations_grid_layout_3)
        self.constellations.addTab(self.constellations_widget_3, 'After Viterbi-Viterbi Algorithm')
        self.top_layout.addWidget(self.constellations)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(quad_rate/samp_rate),
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(quad_rate/samp_rate),
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_const_sink_x_3 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_3.set_update_time(0.10)
        self.qtgui_const_sink_x_3.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_3.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_3.enable_autoscale(False)
        self.qtgui_const_sink_x_3.enable_grid(False)
        self.qtgui_const_sink_x_3.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_3_win = sip.wrapinstance(self.qtgui_const_sink_x_3.qwidget(), Qt.QWidget)
        self.constellations_layout_3.addWidget(self._qtgui_const_sink_x_3_win)
        self.qtgui_const_sink_x_2 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_2.set_update_time(0.10)
        self.qtgui_const_sink_x_2.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_2.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_2.enable_autoscale(False)
        self.qtgui_const_sink_x_2.enable_grid(False)
        self.qtgui_const_sink_x_2.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_2_win = sip.wrapinstance(self.qtgui_const_sink_x_2.qwidget(), Qt.QWidget)
        self.constellations_layout_2.addWidget(self._qtgui_const_sink_x_2_win)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.qwidget(), Qt.QWidget)
        self.constellations_layout_1.addWidget(self._qtgui_const_sink_x_1_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.constellations_layout_0.addWidget(self._qtgui_const_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
            sps,
            taps=tx_taps,
            flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                quad_rate,
                50000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                quad_rate,
                50000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.iir_filter_xxx_0 = filter.iir_filter_ffd([1.0001, -1], [1,1], True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 2*3.14159653/100, rx_taps, 32, 16, 1.5, 1)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(4, 1.414, 5000e-6, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(((1+1j),(1-1j),(-1-1j),(-1+1j)), 1)
        self.blocks_vco_c_0 = blocks.vco_c(samp_rate, -1, 1)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_float*1, '127.0.0.1', 12345, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_float*1, '127.0.0.1', 12345, 1472, True)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_ff(0.25)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(0.25)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.5)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_exponentiate_const_cci_0_0 = blocks.exponentiate_const_cci(4, 1)
        self.blocks_exponentiate_const_cci_0 = blocks.exponentiate_const_cci(4, 1)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, 10)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(quad_rate/symb_rate))
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_arg_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(quad_rate, analog.GR_SIN_WAVE, 110000, -1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(quad_rate, analog.GR_COS_WAVE, 110000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(quad_rate, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 4, 1000))), True)
        self.analog_phase_modulator_fc_0 = analog.phase_modulator_fc(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.analog_phase_modulator_fc_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_exponentiate_const_cci_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_exponentiate_const_cci_0_0, 0), (self.blocks_complex_to_arg_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.qtgui_const_sink_x_3, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.analog_phase_modulator_fc_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_exponentiate_const_cci_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.qtgui_const_sink_x_2, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.blocks_exponentiate_const_cci_0_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_pfb_clock_sync_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "end_to_end")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_rx_taps(firdes.root_raised_cosine(40, 32*self.samp_rate, self.symb_rate, 0.99, 11*self.sps*32))
        self.set_samp_rate(self.symb_rate*self.sps)
        self.set_tx_taps(firdes.root_raised_cosine(40, self.samp_rate, self.symb_rate, 0.99, 11*self.sps*32))
        self.blocks_delay_0.set_dly(int(self.quad_rate/self.symb_rate))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rx_taps(firdes.root_raised_cosine(40, 32*self.samp_rate, self.symb_rate, 0.99, 11*self.sps*32))
        self.set_samp_rate(self.symb_rate*self.sps)
        self.set_tx_taps(firdes.root_raised_cosine(40, self.samp_rate, self.symb_rate, 0.99, 11*self.sps*32))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_quad_rate(5*self.samp_rate)
        self.set_rx_taps(firdes.root_raised_cosine(40, 32*self.samp_rate, self.symb_rate, 0.99, 11*self.sps*32))
        self.set_tx_taps(firdes.root_raised_cosine(40, self.samp_rate, self.symb_rate, 0.99, 11*self.sps*32))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_tx_taps(self):
        return self.tx_taps

    def set_tx_taps(self, tx_taps):
        self.tx_taps = tx_taps
        self.pfb_arb_resampler_xxx_0.set_taps(self.tx_taps)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps(self.rx_taps)

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.quad_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.quad_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.quad_rate)
        self.blocks_delay_0.set_dly(int(self.quad_rate/self.symb_rate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.quad_rate, 50000, 10000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.quad_rate, 50000, 10000, window.WIN_HAMMING, 6.76))

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)




def main(top_block_cls=end_to_end, options=None):

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
