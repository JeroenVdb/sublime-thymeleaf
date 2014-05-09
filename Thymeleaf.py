import sublime, sublime_plugin

class ThymeleafCommand(sublime_plugin.WindowCommand):

	def run(self, **args):

		print("jdksqfjlk")

class ThymeleafCompleteEvents(sublime_plugin.EventListener):

	completions = []

	def __init__(self):

		print("I see this only once!")

		# Get Sublime completions from the settings file

		self.sublimeCompletions = sublime.load_settings('Thymeleaf.sublime-completions').get('completions')

		print(self.sublimeCompletions)

		for completion in self.sublimeCompletions:

			_completion = self.make_completion(completion['trigger'], completion['contents'])

			self.completions.append(_completion)

	def make_completion(self, trigger, content):

		return (trigger, content)

	#
	# Autocomplete suggestions
	#
	def on_query_completions(self, view, prefix, locations):

		inHtmlTag = view.match_selector(locations[0], 'meta.tag.block.any.html')

		if inHtmlTag:

			return (self.completions, sublime.INHIBIT_EXPLICIT_COMPLETIONS)
