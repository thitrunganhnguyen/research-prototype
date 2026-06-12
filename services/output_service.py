def print_sources(search_results):

    print("\n========== SOURCES ==========")

    for index, source in enumerate(search_results, start=1):

        print(f"\n[{index}] {source.get('title')}")
        print(source.get("url"))


def print_result(result):

    print("\n========== RESEARCH RESULT ==========\n")

    print(result)