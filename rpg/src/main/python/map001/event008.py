# -*- coding: utf-8 -*-

from java.awt import Font
from util import *
from game.rpg.process.event import *


if __name__ == '__main__':
    # font
    font_file = Loader.getResourceAsFile("font/mother2.TTF")
    font = Font.createFont(Font.TRUETYPE_FONT, font_file).deriveFont(float(13.0))
    EventCommand.setMessageFont(font)

    # text
    EventCommand.showText(u"マザー２\nやってんだけど\nおもしろいね\nさすがに\nキムタクがCMしてた\nだけのことはあるな\fおとなも\nこどもも\nおねーさんも")