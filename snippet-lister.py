import sublime, sublime_plugin
import os
from re import split



class ListerSnippetCommand(sublime_plugin.TextCommand):
	def get_langage(self):
		langage = split(r'[\.\/]', self.view.settings().get('syntax'))
		langage = langage[-2].lower()
		return langage

	def m(self, t, s="md"):
		t = str(t)
		if s == "md":
			sublime.message_dialog(t)
		elif s == "sm":
			sublime.status_message(t)
		elif s == "em":
			sublime.error_message(t)

	def open_file(self, index):
		if index != -1:
			fileName = self.listFileName[index]
			if not '/' in fileName: # it s not a folder
				if fileName != "..":
					self.window.open_file(os.path.join(self.pathToFile, fileName))
				else:
					self.list_dir("..")
			else:
				self.list_dir(fileName)

	def list_dir(self, extra_folder=None):
		if extra_folder == "..":
			# just read it ;)
			nb = 2 if os.getcwd()[-1] == '/' else 1

			path = os.getcwd().split( os.sep )
			os.chdir( os.sep.join(path[0:-nb]) )

		elif extra_folder is not None: # secure
			os.chdir( os.path.join(os.getcwd(), extra_folder) )

		files = os.listdir()
		listFileName = []
		listFolder = []
		for file in files:
			if os.path.isfile(file):
				listFileName.append(file)
			else:
				listFolder.append(file)

		for i, folder in enumerate(listFolder):
			listFolder[i] = str(folder) + '/'

		self.listFileName = listFolder
		self.listFileName.extend(listFileName)
		self.listFileName.insert(0, "..")

		self.pathToFile = os.getcwd()
		self.window.show_quick_panel(self.listFileName, self.open_file, sublime.KEEP_OPEN_ON_FOCUS_LOST)

	def run(self, edit):

		self.settings = sublime.load_settings("snippet-lister.sublime-settings")



		self.window = self.view.window()
		# go in the right folder
		os.chdir(sublime.packages_path())
		langage = self.get_langage()
		path = ['Packages', 'User', self.settings.get("main_snippet_folder_name", "snippet"), langage]
		for folder in path:
			directories = os.listdir()
			if folder in directories:
				os.chdir( os.path.join(os.getcwd(), folder) )

		# list snippet and extra folder
		self.list_dir()

		self.edit = edit
