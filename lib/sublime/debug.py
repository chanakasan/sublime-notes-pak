import sublime

def alert(value, error=False):
  msg = str(value)
  if error:
    sublime.error_message(msg)
  else:
    sublime.message_dialog(msg)