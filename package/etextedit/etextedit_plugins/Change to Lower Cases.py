def change_to_lower_cases(event=None):
    buffer = event.app.current_buffer if event is not None else text_field.buffer
    selectedText = buffer.cut_selection().text
    content = selectedText if selectedText else buffer.text
    content = content.lower()
    # insert the changes
    buffer.insert_text(content)
    # Repaint the application; get_app().invalidate() does not work here
    get_app().reset()