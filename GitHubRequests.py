import requests


def get_repos(lang, size):
    """
    Function that receive a programming language to filter by and a number of repositories to return
    and return the highest ranked repositories in this language
    :param lang: repos language
    :param size: number of repositories to return
    :return: list of repos
    """
    res = requests.get("https://api.github.com/search/repositories?q=language:" + lang + "&sort=stars&per_page=" + str(size))
    res = res.json()['items']
    return [repo for repo in res]


def print_repos(lang, size):
    """
     This function calls get_repos function and print the repos name with it stars number order by highest stars number
    :param lang: repositories language
    :param size: number of repos to print
    """
    for rep in get_repos(lang, size):
        print(f"{rep['name']} is a Python repo with {rep['stargazers_count']} stars")


if __name__ == '__main__':
    print_repos('Python', 20)


