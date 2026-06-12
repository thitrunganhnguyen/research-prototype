from dotenv import load_dotenv

from services.llm_service import create_llm
from services.prompt_service import build_research_prompt
from services.search_service import search_web
from services.logger import log
from services.output_service import (
    print_sources,
    print_result,
)


def run_research(question):

    log("Start web search")

    search_results = search_web(question)

    print_sources(search_results)

    log("Search completed")

    llm = create_llm()

    prompt = build_research_prompt(
        question=question,
        search_results=search_results
    )

    log("Generate answer")

    response = llm.invoke(prompt)

    log("Finished")

    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content


def main():

    load_dotenv()

    question = input("Research question: ")

    result = run_research(question)

    print_result(result)


if __name__ == "__main__":
    main()