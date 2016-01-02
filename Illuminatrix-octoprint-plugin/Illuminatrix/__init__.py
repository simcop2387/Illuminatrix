# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask
import os
from subprocess import call,Popen

class IlluminatrixPlugin(octoprint.plugin.StartupPlugin,
			octoprint.plugin.TemplatePlugin,
			octoprint.plugin.BlueprintPlugin):

	def __init__(self):
		pass

	def issueCommand(self, cmd_str):
		Popen("echo -n \""+cmd_str+";\" > /dev/ttyUSB0", shell=True)
		return flask.make_response("Illuminatrix "+cmd_str+" mode", 750)

	##StartupPlugin
	def on_after_startup(self):
		self._logger.info("Illuminatrix plugin lives")

	##TemplatePlugin
	def get_template_configs(self):
		return [
			dict(type="tab", template="Illuminatrix_tab.jinja2")
		]

	##BlueprintPlugin
	@octoprint.plugin.BlueprintPlugin.route("/on", methods=["GET"])
	def on(self):
		return self.issueCommand("ON")

	##BlueprintPlugin
	@octoprint.plugin.BlueprintPlugin.route("/off", methods=["GET"])
	def off(self):
		return self.issueCommand("OFF")

	##BlueprintPlugin
	@octoprint.plugin.BlueprintPlugin.route("/white", methods=["GET"])
	def white(self):
		return self.issueCommand("WHITE")

	##BlueprintPlugin
        @octoprint.plugin.BlueprintPlugin.route("/red", methods=["GET"])
        def red(self):
                return self.issueCommand("RED")

	##BlueprintPlugin
        @octoprint.plugin.BlueprintPlugin.route("/green", methods=["GET"])
        def green(self):
                return self.issueCommand("GREEN")

	##BlueprintPlugin
        @octoprint.plugin.BlueprintPlugin.route("/blue", methods=["GET"])
        def blue(self):
                return self.issueCommand("BLUE")



	def is_blueprint_protected(self):
		return False

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginIlluminatrix"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Illuminatrix"
__plugin_implementation__ = IlluminatrixPlugin()
