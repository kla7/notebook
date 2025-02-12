import streamlit as st
from notebook import NoteBook

nb = NoteBook('json')


def clear_add():
    """Clear text from text input elements after a note has been added."""
    st.session_state.note_name = st.session_state.note_name_input
    st.session_state.note_name_input = ""
    st.session_state.note_content = st.session_state.note_content_input
    st.session_state.note_content_input = ""


st.set_page_config(page_title="NoteBook", page_icon="📒")

st.title('📒 NoteBook')

search_term = st.sidebar.text_input(label="Search term")
st.sidebar.markdown("**Notes** (filtered for search term)")
search_results = nb.find(search_term)
st.sidebar.dataframe(data=search_results, use_container_width=True, hide_index=True)

st.sidebar.divider()

clear = st.sidebar.pills(label="Clear", options="Clear notebook", selection_mode="single", label_visibility="collapsed")

if clear:
    st.sidebar.warning("**THIS ACTION IS IRREVERSIBLE.**\n\nAre you sure you want to clear the notebook?", icon="⚠️")
    if st.sidebar.button(label="Confirm", key="confirm_clear"):
        nb.clear()
        st.rerun()

show_note, add_note = st.tabs(["Show note", "Add note"])

with show_note:
    note_name = st.selectbox(label="Select note", options=nb.notes(), index=None, placeholder="Select note...")

    if note_name:
        note_content = nb[note_name]
        note_container = st.container(border=True)
        note_container.text(note_content)

        st.divider()

        actions = ["Edit", "Delete"]
        selection = st.pills(label="Actions", options=actions, selection_mode="single")

        if selection == "Edit":
            new_note_name = st.text_input(label="Note name", value=note_name, label_visibility="collapsed")
            new_note_content = st.text_area(label="Note content", value=note_content, label_visibility="collapsed")

            if st.button("Save"):
                if new_note_name != note_name and new_note_content != note_content:
                    nb.edit(note_name, new_note_content)
                    nb.rename(note_name, new_note_name)
                elif new_note_content != note_content:
                    nb.edit(note_name, new_note_content)
                elif new_note_name != note_name:
                    nb.rename(note_name, new_note_name)
                st.rerun()

        if selection == "Delete":
            st.warning(body="Are you sure you want to delete this note?")
            if st.button(label="Confirm", key="delete_note"):
                nb.delete(note_name)
                st.rerun()

with add_note:
    if "note_name" not in st.session_state:
        st.session_state.note_name = ""
    if "note_content" not in st.session_state:
        st.session_state.note_content = ""

    note_name = st.text_input(label="Note name", label_visibility="collapsed", key="note_name_input")
    note_content = st.text_area(label="Note content", label_visibility="collapsed", key="note_content_input")

    add_button = st.button(label="Add note", on_click=clear_add)

    if add_button and st.session_state.note_name:
        nb.add(st.session_state.note_name, st.session_state.note_content)
        st.rerun()
