import sublime, sublime_plugin, os, subprocess
 
class OpenFolderInNautilusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            file_name = self.view.file_name()
            subprocess.Popen(["nautilus", file_name])