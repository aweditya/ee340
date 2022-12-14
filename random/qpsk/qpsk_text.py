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
from gnuradio.filter import pfb



from gnuradio import qtgui

class qpsk_text(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "qpsk_text")

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
        self.symb_rate = symb_rate = 25000
        self.sps = sps = 4
        self.samp_rate = samp_rate = sps*symb_rate
        self.nfilts = nfilts = 32
        self.excess_bw = excess_bw = 0.4
        self.tx_taps = tx_taps = firdes.root_raised_cosine(nfilts, samp_rate, symb_rate, excess_bw, 11*nfilts*32)
        self.rx_taps = rx_taps = firdes.root_raised_cosine(nfilts, 32*samp_rate, symb_rate, excess_bw, 11*nfilts*32)
        self.rx_constellation = rx_constellation = digital.constellation_calcdist([1+0j, 0+1j, -1+0j, 0-1j], [0, 1, 2, 3],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.quad_rate = quad_rate = 5*samp_rate

        ##################################################
        # Blocks
        ##################################################
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
                70000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                quad_rate,
                70000,
                10000,
                window.WIN_HAMMING,
                6.76))
        self.iir_filter_xxx_0 = filter.iir_filter_ccz([1], [1, -0.6, -0.09], True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 2*3.14159/100, rx_taps, 32, 16, 1.5, 1)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(rx_constellation)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(rx_constellation)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(4, 1, 400e-6, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(((1+0j), (0+1j), (-1+0j), (0-1j)), 1)
        self.blocks_unpack_k_bits_bb_1_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, quad_rate,True)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_char*1, 1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 1)
        self.blocks_pack_k_bits_bb_1_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(2)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(0.09)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.6)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/aditya/Projects/iitb/ee340/random/qpsk/in.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/aditya/Projects/iitb/ee340/random/qpsk/out-custom-equalization.txt', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/aditya/Projects/iitb/ee340/random/qpsk/out-cma.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 40)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 20)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(quad_rate, analog.GR_SIN_WAVE, 100000, -1, 0, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(quad_rate, analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(quad_rate, analog.GR_COS_WAVE, 100000, 1, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_unpack_k_bits_bb_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_pack_k_bits_bb_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1_0, 0), (self.blocks_pack_k_bits_bb_1_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_skiphead_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.iir_filter_xxx_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.digital_pfb_clock_sync_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qpsk_text")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, 32*self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))
        self.set_samp_rate(self.sps*self.symb_rate)
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_samp_rate(self.sps*self.symb_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_quad_rate(5*self.samp_rate)
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, 32*self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, 32*self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rx_taps(firdes.root_raised_cosine(self.nfilts, 32*self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))
        self.set_tx_taps(firdes.root_raised_cosine(self.nfilts, self.samp_rate, self.symb_rate, self.excess_bw, 11*self.nfilts*32))

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

    def get_rx_constellation(self):
        return self.rx_constellation

    def set_rx_constellation(self, rx_constellation):
        self.rx_constellation = rx_constellation

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.quad_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.quad_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.quad_rate)
        self.blocks_throttle_0.set_sample_rate(self.quad_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.quad_rate, 70000, 10000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.quad_rate, 70000, 10000, window.WIN_HAMMING, 6.76))




def main(top_block_cls=qpsk_text, options=None):

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
