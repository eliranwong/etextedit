# The file name of this plugin is 'Change to Upper Cases.py'
# the function name must match the name of the plugin file, with all characters changed to lower cases and spaces replaced with '_'.
def change_to_upper_cases(event=None):
    # get the buffer of the editable text area
    buffer = event.app.current_buffer if event is not None else text_field.buffer
    # cut the selected text; you may also use buffer.copy_selection().text instead to get the selected text without removing it.
    selectedText = buffer.cut_selection().text
    # get the whole text if there is no text being selected.
    content = selectedText if selectedText else buffer.text
    # change the text to upper cases
    content = content.upper()
    # insert the changes
    buffer.insert_text(content)
    # Repaint the application; get_app().invalidate() does not work here
    get_app().reset()