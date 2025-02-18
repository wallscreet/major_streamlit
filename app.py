import streamlit as st
from src.db import init_db, add_note, get_notes


# Initialize the database on first run
init_db()

# Streamlit UI
st.title("📝 Simple Notes App")

# Using session state to handle input clearing
if "note_text" not in st.session_state:
    st.session_state.note_text = ""

# Input field
note = st.text_area("Write your note:", value=st.session_state.note_text, height=100)

# Submit button
if st.button("Save Note"):
    if note.strip():
        add_note(note.strip())
        st.success("Note saved!")
        st.session_state.note_text = ""  # Clear input field
        st.rerun()  # Corrected from experimental_rerun()
    else:
        st.warning("Please enter a valid note.")

# Display stored notes
st.subheader("📜 Your Notes:")
notes = get_notes()

if notes:
    for idx, (note_id, content) in enumerate(notes, start=1):
        st.write(f"**{idx}.** {content}")
else:
    st.info("No notes yet. Start writing!")
