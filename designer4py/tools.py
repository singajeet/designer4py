"""
This module contains classes to build toolitems and toolbar.
This will help implementing a designer framework in any app
and the ouput or the design can be saved as configuration
file which can be reloaded and edited back in the designer.
"""


class Page:
    """An HTML page which will be used to render the content
    on. This is same as widgets4py.base.Page but with limited
    functionality. Use it for development and testing purpose
    only. Use `widgets4py.base.Page' for actual implementation
    and production use
    """

    _canvas = None
    _jquery = 'http://code.jquery.com/jquery-2.1.1.min.js'
    _w2ui = 'http://w2ui.com/src/w2ui-1.5.rc1.min.js'
    _css = 'http://w2ui.com/src/w2ui-1.5.rc1.min.css'

    def __init__(self, canvas):
        self._canvas = canvas

    def render(self):
        content = "<html style='height:100%;width:100%'>"
        content += "\n<head>"
        content += "\n<title>Designer</title>"
        content += "\n<script src='" + self._jquery + "' ></script>"
        content += "\n<script src='" + self._w2ui + "' ></script>"
        content += "\n<link rel='stylesheet' href='" + self._css + "' />"
        content += "\n</head>"
        content += "\n<body>"
        content += self._canvas.render()
        content += "\n</body>"
        content += "\n</html>"
        return content


class Canvas:
    """Canvas is divided into 3 parts - toolbar section, designer section and
    properties section. Toolbar will show all the tools available for designing
    and designer is the section where actual designing can be done
    """

    _toolbar = None
    _designer = None
    _properties = None
    _name = None

    def __init__(self, name, toolbar=None, designer=None, properties=None):
        self._name = name
        self._toolbar = toolbar.render() if toolbar is not None else "toolbar"
        self._designer = designer.render() if designer is not None else "deaigner"
        self._properties = properties.render() if properties is not None else "properties"

    def _attach_script(self):
        script = """
                <script>
                    $(function(){
                        var pstyle = 'border: 1px solid #dfdfdf; padding: 5px;';
                        $('#%s').w2layout({
                            name: '%s',
                            padding: 4,
                            panels: [
                                {type: 'left', size: 200, resizable: true, style: pstyle, content: '%s'},
                                {type: 'main', style: pstyle, content: '%s'},
                                {type: 'bottom', size: 50, resizable: true, style: pstyle, content: '%s'}
                            ]
                        });
                    });
                </script>
                """ % (self._name, self._name, self._toolbar, self._designer, self._properties)
        return script

    def render(self):
        content = "<div id='%s' style='width:100%%;height:100%%'></div>" % (self._name)
        content += "\n" + self._attach_script()
        return content
