from jinja2 import Markup

class CalendarComponents:

    def __init__(self, colour, text):
        self.component =  """
        <div style = "width:100%; display: table; background-color:""" + colour +""";border-radius: 5px; height: 50px; margin:0;" onclick = "openNav()"> 
        <div style = "color:white; font-size: 1.2vw; display: table-cell; vertical-align: middle; text-align: center;">""" \
                          + text + """</div></div>"""



    def render_component(self):
        return Markup(self.component)

