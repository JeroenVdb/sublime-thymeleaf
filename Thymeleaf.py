import sublime, sublime_plugin

class ThymeleafCompleteEvents(sublime_plugin.EventListener):

	completions = []

	def __init__(self):

		thCompletions = [

			('th:include\tThymeleaf', 'th:include="$1"'),
			('th:replace\tThymeleaf', 'th:replace="$1"'),
			('th:each\tThymeleaf', 'th:each="\$\{$1 : $2\}"'),
			('th:if\tThymeleaf', 'th:if="\$\{$1\}"'),
			('th:unless\tThymeleaf', 'th:unless="\$\{$1\}"'),
			('th:switch\tThymeleaf', 'th:switch="\$\{$1\}"'),
			('th:case\tThymeleaf', 'th:case="\$\{$1\}"'),
			('th:object\tThymeleaf', 'th:object="\$\{$1\}"'),
			('th:with\tThymeleaf', 'th:with="\$\{$1\}"'),
			('th:attr\tThymeleaf', 'th:attr="\$\{$1\}"'),
			('th:attrprepend\tThymeleaf', 'th:attrprepend="\$\{$1\}"'),
			('th:attrappend\tThymeleaf', 'th:attrappend="\$\{$1\}"'),
			('th:text\tThymeleaf', 'th:text="\$\{$1\}"'),
			('th:utext\tThymeleaf', 'th:utext="\$\{$1\}"'),
			('th:fragment\tThymeleaf', 'th:fragment="$1"'),
			('th:remove\tThymeleaf', 'th:remove="\$\{$1\}"'),
			('th:inline\tThymeleaf', 'th:inline="\$\{$1\}"'),

			('th:abbr\tThymeleaf', 'th:abbr="\$\{$1\}"'),
			('th:accesskey\tThymeleaf', 'th:accesskey="\$\{$1\}"'),
			('th:alt\tThymeleaf', 'th:alt="\$\{$1\}"'),
			('th:autocomplete\tThymeleaf', 'th:autocomplete="\$\{$1\}"'),
			('th:bgcolor\tThymeleaf', 'th:bgcolor="\$\{$1\}"'),
			('th:cellspacing\tThymeleaf', 'th:cellspacing="\$\{$1\}"'),
			('th:cite\tThymeleaf', 'th:cite="\$\{$1\}"'),
			('th:codebase\tThymeleaf', 'th:codebase="\$\{$1\}"'),
			('th:colspan\tThymeleaf', 'th:colspan="\$\{$1\}"'),
			('th:contenteditable\tThymeleaf', 'th:contenteditable="\$\{$1\}"'),
			('th:datetime\tThymeleaf', 'th:datetime="\$\{$1\}"'),
			('th:dropzone\tThymeleaf', 'th:dropzone="\$\{$1\}"'),
			('th:form\tThymeleaf', 'th:form="\$\{$1\}"'),
			('th:formmethod\tThymeleaf', 'th:formmethod="\$\{$1\}"'),
			('th:frameborder\tThymeleaf', 'th:frameborder="\$\{$1\}"'),
			('th:high\tThymeleaf', 'th:high="\$\{$1\}"'),
			('th:hspace\tThymeleaf', 'th:hspace="\$\{$1\}"'),
			('th:id\tThymeleaf', 'th:id="\$\{$1\}"'),
			('th:label\tThymeleaf', 'th:label="\$\{$1\}"'),
			('th:longdesc\tThymeleaf', 'th:longdesc="\$\{$1\}"'),
			('th:marginheight\tThymeleaf', 'th:marginheight="\$\{$1\}"'),
			('th:maxlength\tThymeleaf', 'th:maxlength="\$\{$1\}"'),
			('th:min\tThymeleaf', 'th:min="\$\{$1\}"'),
			('th:pattern\tThymeleaf', 'th:pattern="\$\{$1\}"'),
			('th:preload\tThymeleaf', 'th:preload="\$\{$1\}"'),
			('th:rev\tThymeleaf', 'th:rev="\$\{$1\}"'),
			('th:rules\tThymeleaf', 'th:rules="\$\{$1\}"'),
			('th:scope\tThymeleaf', 'th:scope="\$\{$1\}"'),
			('th:sizes\tThymeleaf', 'th:sizes="\$\{$1\}"'),
			('th:src\tThymeleaf', 'th:src="\$\{$1\}"'),
			('th:start\tThymeleaf', 'th:start="\$\{$1\}"'),
			('th:summary\tThymeleaf', 'th:summary="\$\{$1\}"'),
			('th:title\tThymeleaf', 'th:title="\$\{$1\}"'),
			('th:value\tThymeleaf', 'th:value="\$\{$1\}"'),
			('th:width\tThymeleaf', 'th:width="\$\{$1\}"'),
			('th:xmllang\tThymeleaf', 'th:xmllang="\$\{$1\}"'),
			('th:accept\tThymeleaf', 'th:accept="\$\{$1\}"'),
			('th:action\tThymeleaf', 'th:action="\$\{$1\}"'),
			('th:archive\tThymeleaf', 'th:archive="\$\{$1\}"'),
			('th:axis\tThymeleaf', 'th:axis="\$\{$1\}"'),
			('th:border\tThymeleaf', 'th:border="\$\{$1\}"'),
			('th:challenge\tThymeleaf', 'th:challenge="\$\{$1\}"'),
			('th:class\tThymeleaf', 'th:class="\$\{$1\}"'),
			('th:codetype\tThymeleaf', 'th:codetype="\$\{$1\}"'),
			('th:compact\tThymeleaf', 'th:compact="\$\{$1\}"'),
			('th:contextmenu\tThymeleaf', 'th:contextmenu="\$\{$1\}"'),
			('th:dir\tThymeleaf', 'th:dir="\$\{$1\}"'),
			('th:enctype\tThymeleaf', 'th:enctype="\$\{$1\}"'),
			('th:formaction\tThymeleaf', 'th:formaction="\$\{$1\}"'),
			('th:formtarget\tThymeleaf', 'th:formtarget="\$\{$1\}"'),
			('th:headers\tThymeleaf', 'th:headers="\$\{$1\}"'),
			('th:href\tThymeleaf', 'th:href="\$\{$1\}"'),
			('th:http-equiv\tThymeleaf', 'th:http-equiv="\$\{$1\}"'),
			('th:keytype\tThymeleaf', 'th:keytype="\$\{$1\}"'),
			('th:lang\tThymeleaf', 'th:lang="\$\{$1\}"'),
			('th:low\tThymeleaf', 'th:low="\$\{$1\}"'),
			('th:marginwidth\tThymeleaf', 'th:marginwidth="\$\{$1\}"'),
			('th:media\tThymeleaf', 'th:media="\$\{$1\}"'),
			('th:name\tThymeleaf', 'th:name="\$\{$1\}"'),
			('th:placeholder\tThymeleaf', 'th:placeholder="\$\{$1\}"'),
			('th:radiogroup\tThymeleaf', 'th:radiogroup="\$\{$1\}"'),
			('th:rows\tThymeleaf', 'th:rows="\$\{$1\}"'),
			('th:sandbox\tThymeleaf', 'th:sandbox="\$\{$1\}"'),
			('th:scrolling\tThymeleaf', 'th:scrolling="\$\{$1\}"'),
			('th:span\tThymeleaf', 'th:span="\$\{$1\}"'),
			('th:srclang\tThymeleaf', 'th:srclang="\$\{$1\}"'),
			('th:step\tThymeleaf', 'th:step="\$\{$1\}"'),
			('th:tabindex\tThymeleaf', 'th:tabindex="\$\{$1\}"'),
			('th:type\tThymeleaf', 'th:type="\$\{$1\}"'),
			('th:valuetype\tThymeleaf', 'th:valuetype="\$\{$1\}"'),
			('th:wrap\tThymeleaf', 'th:wrap="\$\{$1\}"'),
			('th:xmlspace\tThymeleaf', 'th:xmlspace="\$\{$1\}"'),
			('th:accept-charset\tThymeleaf', 'th:accept="\$\{$1\}"'),
			('th:align\tThymeleaf', 'th:align="\$\{$1\}"'),
			('th:audio\tThymeleaf', 'th:audio="\$\{$1\}"'),
			('th:background\tThymeleaf', 'th:background="\$\{$1\}"'),
			('th:cellpadding\tThymeleaf', 'th:cellpadding="\$\{$1\}"'),
			('th:charset\tThymeleaf', 'th:charset="\$\{$1\}"'),
			('th:classid\tThymeleaf', 'th:classid="\$\{$1\}"'),
			('th:cols\tThymeleaf', 'th:cols="\$\{$1\}"'),
			('th:content\tThymeleaf', 'th:content="\$\{$1\}"'),
			('th:data\tThymeleaf', 'th:data="\$\{$1\}"'),
			('th:draggable\tThymeleaf', 'th:draggable="\$\{$1\}"'),
			('th:for\tThymeleaf', 'th:for="\$\{$1\}"'),
			('th:formenctype\tThymeleaf', 'th:formenctype="\$\{$1\}"'),
			('th:frame\tThymeleaf', 'th:frame="\$\{$1\}"'),
			('th:height\tThymeleaf', 'th:height="\$\{$1\}"'),
			('th:hreflang\tThymeleaf', 'th:hreflang="\$\{$1\}"'),
			('th:icon\tThymeleaf', 'th:icon="\$\{$1\}"'),
			('th:kind\tThymeleaf', 'th:kind="\$\{$1\}"'),
			('th:list\tThymeleaf', 'th:list="\$\{$1\}"'),
			('th:manifest\tThymeleaf', 'th:manifest="\$\{$1\}"'),
			('th:max\tThymeleaf', 'th:max="\$\{$1\}"'),
			('th:method\tThymeleaf', 'th:method="\$\{$1\}"'),
			('th:optimum\tThymeleaf', 'th:optimum="\$\{$1\}"'),
			('th:poster\tThymeleaf', 'th:poster="\$\{$1\}"'),
			('th:rel\tThymeleaf', 'th:rel="\$\{$1\}"'),
			('th:rowspan\tThymeleaf', 'th:rowspan="\$\{$1\}"'),
			('th:scheme\tThymeleaf', 'th:scheme="\$\{$1\}"'),
			('th:size\tThymeleaf', 'th:size="\$\{$1\}"'),
			('th:spellcheck\tThymeleaf', 'th:spellcheck="\$\{$1\}"'),
			('th:standby\tThymeleaf', 'th:standby="\$\{$1\}"'),
			('th:style\tThymeleaf', 'th:style="\$\{$1\}"'),
			('th:target\tThymeleaf', 'th:target="\$\{$1\}"'),
			('th:usemap\tThymeleaf', 'th:usemap="\$\{$1\}"'),
			('th:vspace\tThymeleaf', 'th:vspace="\$\{$1\}"'),
			('th:xmlbase\tThymeleaf', 'th:xmlbase="\$\{$1\}"')
		]

		for completion in thCompletions:

			self.completions.append(completion)

	#
	# Autocomplete suggestions
	#
	def on_query_completions(self, view, prefix, locations):

		inHtmlTag = view.match_selector(locations[0], 'text.html.basic, meta.tag.block.any.html, meta.tag.inline.any.html, meta.tag.other.html')

		inAttribute = view.match_selector(locations[0], 'string.quoted.double.html')

		if inHtmlTag and not inAttribute:

			return (self.completions, sublime.INHIBIT_EXPLICIT_COMPLETIONS)
