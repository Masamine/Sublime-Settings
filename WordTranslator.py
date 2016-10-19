# -*- coding: utf-8 -*-
import sublime, sublime_plugin
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.5/Resources/Python.app/Contents/MacOS/Python')
from mstranslator import Translator
from future.utils import string_types

class WordTranslatorCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		sel_area = self.view.sel()
		self.view.erase_status('word_translator_error')
		self.view.erase_status('word_translator_result')
		#translator = Translator('sublime_word_translator', 'XP8HbQ9YYgzTeTbmLTFzVry9r+YRXab4MgkG+goNmmY=')
		client = Translator('sublime_word_translator', 'XP8HbQ9YYgzTeTbmLTFzVry9r+YRXab4MgkG+goNmmY=')
		result_txt = client.translate("hello", "jp")

		if sel_area[0].empty():
			self.view.set_status('word_translator_error', "WordTranslator:どこも選択していません。")
		else:
			for i in range(0, len(sel_area)):
				cur_txt    = self.view.substr(sel_area[i])
				#result_txt = translator.translate(cur_txt, "jp")
				#result_txt = translator.translate("Hello", "ja")
				result_txt = 'client.translate("hello", "pt")'
				self.view.set_status('word_translator_result', cur_txt + "を" + result_txt + "に翻訳したぞ")

