import streamlit as st
from pages import search_engine_page, document_page


if "selected_record" not in st.session_state:
    st.session_state["selected_record"] = None


def set_record(record):
    st.session_state["selected_record"] = record


if not st.session_state["selected_record"]:  # search engine page
    st.set_page_config(
        page_title="HuggingFace Search Engine",
        page_icon="🔎",
        layout="wide",
        initial_sidebar_state="auto",
        # menu_items={
        #     "Get Help": "https://www.extremelycoolapp.com/help",
        #     "Report a bug": "https://www.extremelycoolapp.com/bug",
        #     "About": "# This is a header. This is an *extremely* cool app!",
        # },
    )
    search_engine_page()

else:  # a record has been selected
    document_page()


st.markdown(
    """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
# position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made with ❤️ by <b>Nouamane Tazi</b></p>
</div>
""",
    unsafe_allow_html=True,
)
