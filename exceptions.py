"""
exceptions
Based on plotly exception module <https://github.com/plotly/python-api/blob/master/plotly/exceptions.py>.
==========

A module that contains MCP9809 exception hierarchy.

message (required!) (should be root message + caller message)
info: (required!)
    path_to_error (required!)
    minimal_message (required!)

- minimal_message is set inside this module, should not be set elsewhere

- message is set inside this module, should not be set elsewhere


"""

class MCP9809_Error:

  def __init__(self, message='', path=None, notes=None, plain_message=''):
    self.message = message
        self.plain_message=plain_message
        if isinstance(path, list):
            self.path = path
        elif path is None:
            self.path = []
        else:
            self.path = [path]
        if isinstance(notes, list):
            self.notes = notes
        elif notes is None:
            self.notes = []
        else:
            self.notes = [notes]
        super(MCP9809_Error, self).__init__(message)
        self.prepare()
