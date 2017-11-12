# Harrison Satcher
# November 11, 2017
# WikiWebScraper
# # # # # # # # # # # 
# Scrape a wikipedia page for its links, and follow those links' links,
# showing connection between them in an auto-generated pdf.
import wikipedia # https://pypi.python.org/pypi/wikipedia/
import re
from graphviz import Digraph # https://pypi.python.org/pypi/graphviz
# http://graphviz.readthedocs.io/en/stable/manual.html
# http://www.graphviz.org/Documentation/dotguide.pdf


# Testcase: "Crawford Purchase"
# Testcase2: "Cabot Science Library"
# Testcase3: "Penicillium raistrickii"
i = 0
myarr = list()
target = raw_input("What are you interested in? ")
dot = Digraph(comment = target)
targetloc = str(i)
dot.node(targetloc, target)
myarr.append(target)
target = re.sub(" ", "_", target)
target_page = wikipedia.page(target)
links = target_page.links
print("Title, level1: " + target)
print links
for link in links:
  i += 1
  try:
    page2 = wikipedia.page(link)
    title2 = page2.title.encode('ascii', 'ignore').decode('ascii')
    print("Title, level2: " + title2)
    loc = str(i)
    dot.node(loc, title2)
    myarr.append(title2)
    dot.edge(targetloc, loc)
    # links2 = page2.links
    # for link2 in links2:
    #   i += 1
    #   try: 
    #     page3 = wikipedia.page(link2)
    #     title3 = page3.title.encode('ascii', 'ignore').decode('ascii')
    #     print("Title, level3: " + title3)
    #     loc2 = str(i)
    #     if title3 in myarr:
    #       locBack = str(myarr.index(title3))
    #       dot.edge(loc2, locBack)
    #     else:
    #       dot.node(loc2, title3)
    #       myarr.append(title3)
    #       dot.edge(loc, loc2)
    #   except: 
    #     print("Error accessing page: " + link.encode('ascii', 'ignore').decode('ascii'))
  except:
    print("Error accessing page: " + link.encode('ascii', 'ignore').decode('ascii'))
  # TODO: collapse into one loop with before...append links to one list
  
# print myarr
print dot.source
f = open("test-output/"+target+".gv", "w")
f.write(dot.source)
dot.render('test-output/'+target+'.gv', view=True)
