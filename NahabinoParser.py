from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class NahabinoParser(HTMLParser):
    def __init__(self):
        self.stack = []
        HTMLParser.__init__(self)
        self.result_str = unicode()
        self.list_coast = []

    def handle_starttag(self, tag, attrs):

        for attr in attrs:
            if (attr[1] == 'serp-item__price-col' and attr[0] == 'class') or \
                    (tag == 'div' and attr[1] == 'serp-item__solid' and attr[0] == 'class' and  len(self.stack) > 0) or \
                    (tag == 'div' and attr[1] == 'serp-item__prop' and attr[0] == 'class' and len(self.stack) > 0):
                self.stack.append(attr[1])
#                self.result_str = self.result_str + '<div ' + attr[0] + '="' + attr[1] + '" >'



    def get_result(self):
        return self.result_str

    def handle_endtag(self, tag):
        if tag == 'div' and len(self.stack) > 0:
            self.stack.pop()
 #           self.result_str = self.result_str + "</" + tag + ">"

    def handle_data(self, data):
        if len(self.stack) > 0 and self.stack[len(self.stack) - 1] == 'serp-item__solid':
            self.result_str = self.result_str + data



#    def handle_comment(self, data):
#        print "Comment  :", data
#        self.result_str = self.result_str + "<!--" + data + "-->"

#    def handle_entityref(self, name):
#        c = unichr(name2codepoint[name])
#        self.result_str = self.result_str + c

#    def handle_charref(self, name):
#        if name.startswith('x'):
#            c = unichr(int(name[1:], 16))
#        else:
#            c = unichr(int(name))
#        self.result_str = self.result_str + c

#    def handle_decl(self, data):
#        self.result_str = self.result_str + "<!" + data + ">"
