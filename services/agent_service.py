from services.llm_service import create_llm
from services.search_service import search_web


def format_search_results(results):
    formatted = ""

    for index, result in enumerate(results, start=1):
        formatted += f"""
Result {index}:
Title: {result.get("title")}
URL: {result.get("url")}
Snippet: {result.get("snippet")}
"""

    return formatted


def run_agent_research(question):
    llm = create_llm()

    planning_prompt = f"""
You are a research planner.

Create up to 3 search queries for this research question.
Return only the search queries, one per line.

Question:
{question}
"""

    planning_response = llm.invoke(planning_prompt)

    if isinstance(planning_response.content, list):
        query_text = planning_response.content[0]["text"]
    else:
        query_text = planning_response.content

    queries = [
        line.strip("- ").strip()
        for line in query_text.splitlines()
        if line.strip()
    ][:3]

    all_results = []

    for query in queries:
        results = search_web(query)
        all_results.extend(results)

    sources = format_search_results(all_results)

    final_prompt = f"""
You are a professional research agent.

Use only the provided sources to answer the research question.
Do not invent information.
If the sources are not enough, say that clearly.

Research question:
{question}

Sources:
{sources}

Return the answer in this structure:

# Summary

# Key Findings

# Advantages

# Risks / Limitations

# Conclusion

# Sources
List the used sources with title and URL.
"""

    final_response = llm.invoke(final_prompt)

    if isinstance(final_response.content, list):
        return final_response.content[0]["text"]

    return final_response.content