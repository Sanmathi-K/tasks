import streamlit as st

# Initialize session state for notes
if 'notes' not in st.session_state:
    st.session_state.notes = {}

def display_menu():
    st.title("Notes Application")
    menu_options = ["View notes", "Add a new note", "Search for a note by title", "Delete a note", "Exit"]
    choice = st.selectbox("Choose an option:", menu_options)
    return choice

def view_notes():
    st.subheader("View Notes")
    if not st.session_state.notes:
        st.write("No notes available.")
    else:
        for title, content in st.session_state.notes.items():
            st.write(f"**Title:** {title}")
            st.write(f"**Content:** {content}\n")

def add_note():
    st.subheader("Add a New Note")
    title = st.text_input("Enter note title:").strip()
    if title:
        if title in st.session_state.notes:
            st.write("Note with this title already exists.")
        else:
            content = st.text_area("Enter note content:").strip()
            if content:
                st.session_state.notes[title] = content
                st.write("Note added.")
            else:
                st.write("Note content cannot be empty.")

def search_note():
    st.subheader("Search for a Note by Title")
    title = st.text_input("Enter note title to search:").strip()
    if title:
        if title in st.session_state.notes:
            st.write(f"**Title:** {title}")
            st.write(f"**Content:** {st.session_state.notes[title]}")
        else:
            st.write("Note not found.")

def delete_note():
    st.subheader("Delete a Note")
    title = st.text_input("Enter note title to delete:").strip()
    if title:
        if title in st.session_state.notes:
            del st.session_state.notes[title]
            st.write("Note deleted.")
        else:
            st.write("Note not found.")

def main():
    choice = display_menu()
    if choice == "View notes":
        view_notes()
    elif choice == "Add a new note":
        add_note()
    elif choice == "Search for a note by title":
        search_note()
    elif choice == "Delete a note":
        delete_note()
    elif choice == "Exit":
        st.write("Exiting the application.")

if __name__ == "__main__":
    main()
