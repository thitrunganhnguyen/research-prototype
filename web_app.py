import streamlit as st
from dotenv import load_dotenv

from services.llm_service import create_llm
from services.prompt_service import build_research_prompt
from services.search_service import search_web
from services.agent_service import run_agent_research


load_dotenv()

st.set_page_config(
    page_title="Research Assistant",
    page_icon="🔎",
    layout="wide"
)

st.markdown("""
<style>

.main .block-container {
    max-width: 1100px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

.hero {
    text-align: center;
    padding-top: 1rem;
    padding-bottom: 1.8rem;
}

.hero h1 {
    font-size: 48px;
    margin-bottom: 0.3rem;
}

.subtitle {
    font-size: 18px;
    opacity: 0.75;
}

.stButton button {
    height: 46px;
    border-radius: 14px;
    font-size: 16px;
    transition: 0.2s;
}

.stButton button:hover {
    transform: translateY(-1px);
}

button[kind="primary"] {
    background: #4b4a4aab !important;
    color: white !important;
    border: 1px solid #6b6a6a !important;
    font-weight: 700 !important;
    box-shadow: 0 6px 18px rgba(75, 74, 74, 0.22) !important;
}

button[kind="primary"]:hover {
    background: #3f3e3e !important;
    border-color: #7a7979 !important;
    color: white !important;
}

[data-testid="stTextArea"] textarea {
    border-radius: 18px !important;
    border: 1px solid #4b5563 !important;
    box-shadow: none !important;
    outline: none !important;
}

[data-testid="stTextArea"] textarea:focus,
[data-testid="stTextArea"] textarea:focus-visible,
[data-testid="stTextArea"] textarea:hover {
    border: 1px solid #4b5563 !important;
    box-shadow: 0 0 0 1px #4b5563 !important;
    outline: none !important;
}

[data-baseweb="textarea"],
[data-baseweb="textarea"]:focus-within {
    border-color: #4b5563 !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

if "result" not in st.session_state:
    st.session_state.result = None

if "question" not in st.session_state:
    st.session_state.question = ""

if "sources" not in st.session_state:
    st.session_state.sources = []

if "mode" not in st.session_state:
    st.session_state.mode = "⚡ Fast Research"

st.markdown("""
<div class="hero">

# 🔎 Research Assistant

<div class="subtitle">
Ask anything. Search. Analyze. Summarize.
</div>

</div>
""", unsafe_allow_html=True)

mode = st.radio(
    "Research mode",
    ["⚡ Fast Research", "🧠 Agent Research"],
    horizontal=True
)

question = st.text_area(
    "",
    value=st.session_state.question,
    placeholder="Ask a research question...",
    height=110
)

st.markdown("#### Try examples")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("SaaS ERP advantages", use_container_width=True):
        st.session_state.question = "What are the main advantages of SaaS ERP systems?"
        st.rerun()

with c2:
    if st.button("Latest AI trends", use_container_width=True):
        st.session_state.question = "What are the latest AI trends in business applications?"
        st.rerun()

with c3:
    if st.button("Cloud architecture", use_container_width=True):
        st.session_state.question = "What are the main principles of modern cloud architecture?"
        st.rerun()

left_space, button_col, right_space = st.columns([1.2, 1, 1.2])

with button_col:
    start = st.button(
        "🚀 Start Research",
        use_container_width=True,
        type="primary"
    )

if start:
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        st.session_state.question = question
        st.session_state.mode = mode
        st.session_state.result = None
        st.session_state.sources = []

        if mode == "⚡ Fast Research":
            with st.status("Running fast research...", expanded=True) as status:
                st.write("Searching sources...")

                search_results = search_web(question)
                st.session_state.sources = search_results

                st.write(f"{len(search_results)} sources found")
                st.write("Generating report...")

                llm = create_llm()
                prompt = build_research_prompt(
                    question=question,
                    search_results=search_results
                )

                response = llm.invoke(prompt)

                if isinstance(response.content, list):
                    result = response.content[0]["text"]
                else:
                    result = response.content

                st.session_state.result = result

                status.update(
                    label="Fast research completed",
                    state="complete"
                )

        if mode == "🧠 Agent Research":
            with st.status("Running agent research...", expanded=True) as status:
                st.write("Planning search queries...")
                st.write("Agent mode may use more API requests.")

                result = run_agent_research(question)

                st.session_state.result = result

                status.update(
                    label="Agent research completed",
                    state="complete"
                )

if st.session_state.result:
    st.divider()

    if st.session_state.mode == "⚡ Fast Research":
        left, right = st.columns([2.4, 1])

        with left:
            st.markdown("## Research Report")
            st.markdown(st.session_state.result)

            st.download_button(
                "⬇ Download Report",
                st.session_state.result,
                "research_report.md",
                mime="text/markdown",
                type="primary"
            )

        with right:
            st.markdown("## Sources")

            for index, source in enumerate(
                st.session_state.sources,
                start=1
            ):
                with st.container(border=True):
                    st.markdown(f"**{index}. {source.get('title')}**")
                    st.link_button("Open", source.get("url"))
                    st.caption(source.get("snippet"))

    else:
        st.markdown("## Agent Research Report")
        st.markdown(st.session_state.result)

        st.download_button(
            "⬇ Download Agent Report",
            st.session_state.result,
            "agent_research_report.md",
            mime="text/markdown",
            type="primary"
        )