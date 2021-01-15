from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def feed(self, html):
        multiLineComment = False
        for line in html.split("\n"):
            if(line[:4] == "<!--") and line[-3:] == "-->":
                print(">>> Single-line Comment")
                print(line[4:-3])
            
            if(line[:4] == "<!--") and line[-3:] != "-->":
                multiLineComment = True
                print(">>> Multi-line Comment")
                print(line[4:])
            if(line[:4] != "<!--") and line[-3:] == "-->":
                multiLineComment = False
                print(line[:-3])
            if(line[:4] != "<!--") and line[-3:] != "-->" and multiLineComment is True:
                print(line)
                
            if(multiLineComment is False):
                if(line[:5] == "<div>") and line[-6:] == "</div>":
                    print(">>> Data")
                    print(line[5:-6])

  
  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
