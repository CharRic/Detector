# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: Detector.py
@ Version 1.1
@ information: Interface instantiation ;Start function
'''
import sys

from PyQt5.QtWidgets import QApplication

from Ui.DetectorUi import DetectorUi


def main():
    app = QApplication(sys.argv)
    detector = DetectorUi()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
