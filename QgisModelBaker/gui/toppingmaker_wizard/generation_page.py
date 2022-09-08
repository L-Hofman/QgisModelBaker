# -*- coding: utf-8 -*-
"""
/***************************************************************************
                              -------------------
        begin                : 2022-08-01
        git sha              : :%H$
        copyright            : (C) 2022 by Dave Signer
        email                : david at opengis ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.core import QgsProject
from qgis.PyQt.QtWidgets import QWizardPage

import QgisModelBaker.utils.gui_utils as gui_utils
from QgisModelBaker.utils import gui_utils

PAGE_UI = gui_utils.get_ui_class("toppingmaker_wizard/generation.ui")


class GenerationPage(QWizardPage, PAGE_UI):
    def __init__(self, parent, title):
        QWizardPage.__init__(self)

        self.toppingmaker_wizard = parent

        self.setupUi(self)

        self.setTitle(title)
        self.setStyleSheet(gui_utils.DEFAULT_STYLE)
        self.run_generate_button.clicked.connect(self.generate)

    def generate(self):
        ilidata_file = self.toppingmaker_wizard.topping_maker.bakedycakedy(
            QgsProject.instance()
        )
        if ilidata_file:
            self.progress_bar.setValue(100)
            self.progress_bar.setFormat(self.tr("Topping generated 🧁"))
            self.progress_bar.setTextVisible(True)
            self.info_text_edit.setText(f"Find the ilidata.xml here:\n{ilidata_file}")
        else:
            self.progress_bar.setValue(0)
            self.progress_bar.setFormat(self.tr("Topping not generated 💩"))
            self.progress_bar.setTextVisible(True)
