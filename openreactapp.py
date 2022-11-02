import re
from unittest import result

folder = open("/Users/renaudfradin/Downloads/joon-38475a.webflow/index.html", "r")
# print("print folder",folder)
htmlJ = folder.read()

# print("print htmlJ",htmlJ)


def filter_body_for_jsx(html, keep_body_class=True):
  """
  :param html: full JSX page
  :return: full body part of JSX page, in <div></div>
  """
  result = re.search('<body(?:(?: )?(?:className|class)=\"([a-zA-Z0-9_-]*)\")?>((.|\n)*?)<\/body>', html)
  if not result:
      print(html[:3000])
      # tools.write_file("error.html", html)
      raise ValueError("body not found")

  class_name = result.group(1)
  class_property = f" className=\"{class_name}\"" if class_name and keep_body_class else ""
  html = result.group(2)
  return f"<div{class_property}>" + html + "</div>\n"





def html2jsx(html, remove_scripts=True):  # code a factorer, 3 fois meme chose, tools basic, seul differece br a pas d'espace
  """
      IMPORTANT: remove all scripts
  """
  # remove HTML comments
  html = re.sub('<!--(.|\n)*?-->', '', html)

  # close images tags
  regex = '(<img (.|\n)*?)>'  # should work if already closed
  html = re.sub(regex, r"\1/>", html)

  # close br tags
  regex = '(<br(.|\n)*?)>'  # should work if already closed
  html = re.sub(regex, r"\1/>", html)

  # close input tags
  regex = '(<input (.|\n)*?)>'  # should work if already closed
  html = re.sub(regex, r"\1/>", html)

  # close meta tags
  regex = '(<meta (.|\n)*?)>'  # should work if already closed
  html = re.sub(regex, r"\1/>", html)

  # close link tags
  regex = '(<link (.|\n)*?)>'  # should work if already closed
  html = re.sub(regex, r"\1/>", html)

  # remove script tags
  if remove_scripts:
      regex = '<script(.|\n)*?<\/script>'
      html = re.sub(regex, "", html)

  # remove styles
  regex = '(style="(.|\n)*?")'
  html = re.sub(regex, "", html)

  # replace class by className and camel case other features
  html = re.sub('class(=\"[ a-zA-Z0-9_-]*\")', r"className\1", html)
  html = re.sub('srcset(=\"[ :,\.\/a-zA-Z0-9_-]*\")', r"srcSet\1", html)
  html = re.sub('charset(="(?:.|\n)*?")', r"charSet\1", html)
  html = re.sub('autocomplete(="(?:.|\n)*?")', r"autoComplete\1", html)
  html = re.sub('maxlength(="(?:.|\n)*?")', r"maxLength\1", html)
  html = re.sub('crossorigin(="(?:.|\n)*?")', r"crossOrigin\1", html)
  html = re.sub('onclick(="(?:.|\n)*?")', r"onClick\1", html)

  html = html.replace("<head>", "<Head>")
  html = html.replace("</head>", "</Head>")

  # transforms functions int react events handlers
  html = re.sub('onClick=\"([a-zA-Z_]*?)\(\)\"', r"onClick={\1}", html)

  return html

# jsx = html2jsx(htmlJ)
# print(jsx)

# result = filter_body_for_jsx(jsx)
# print(result)
# testchaine = "<body class='body'>"
htmlSplit = htmlJ.split('\n')
# print("print split",htmlJ.split('\n'))
# startBody = htmlJ.startswith("<body")

# print("print html",htmlSplit[10].startswith("<body"))

i = 0
resultaBody = ""
while htmlSplit[i].startswith("<body") == False:
  i=i+1
  print("ligne",i)
  resultaBody = htmlSplit[i]
  
print("resultat body",resultaBody)
  
# print(test.startswith("body"))