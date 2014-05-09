import sublime, sublime_plugin

class ThymeleafCompleteEvents(sublime_plugin.EventListener):

	completions = []

	def __init__(self):

		thCompletions = [
			('th:if\tThymeleaf', 'th:if="$1"'),
			('th:each\tThymeleaf', 'th:each="$1 : $2"'),
		]

		for completion in thCompletions:

			self.completions.append(completion)

	def make_completion(self, trigger, content):

		return (trigger, content)

	#
	# Autocomplete suggestions
	#
	def on_query_completions(self, view, prefix, locations):

		inHtmlTag = view.match_selector(locations[0], 'meta.tag.block.any.html')

		if inHtmlTag:

			return (self.completions, sublime.INHIBIT_EXPLICIT_COMPLETIONS)
