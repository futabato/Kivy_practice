from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path("ダウンロードパス/IPAexfont00301")
LabelBase.register(DEFAULT_FONT, "ipaexg.ttf")


"""
日本語フォントをダウンロード(http://ipafont.ipa.go.jp/node26#jp)
"""