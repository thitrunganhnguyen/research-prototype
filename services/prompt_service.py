def format_sources(search_results):
    formatted = ""

    for index, result in enumerate(search_results, start=1):
        formatted += f"""
Source {index}:
Title: {result.get("title")}
URL: {result.get("url")}
Snippet: {result.get("snippet")}
"""

    return formatted


def build_research_prompt(question, search_results):
    sources = format_sources(search_results)

    return f"""
You are a professional research assistant.

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