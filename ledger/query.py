"""Utilities for GitHub GraphQL querying."""
from functools import lru_cache
from pathlib import Path
from typing import Any


from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
from graphql import DocumentNode

from ledger.config import GitHubConfig


QUERIES = []

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(
  url="https://api.github.com/graphql",
  headers={
    "Authorization": f"bearer {GitHubConfig.token}"
  }
)

# Create a GraphQL client using the defined transport
client = Client(
  transport=transport,
  fetch_schema_from_transport=True
)


@lru_cache()
def load_query(name: str) -> DocumentNode:
    """Load a query from the queries folder."""
    query_file = Path(__file__).parent / f"queries/{name}.gql"

    with query_file.open() as query_data:
        return gql(query_data.read())


def pull_requests(repository_names: list[str]) -> list[dict[str, Any]]:
    """
    Run a GraphQL query for all pull requests in provided repositories.

    This automatically handles any pagination.
    """
    all_prs = []

    for repository in repository_names:
        has_next_page = True
        end_cursor = None

        while has_next_page:
            result = client.execute(load_query("pull_requests"), variable_values={
                "repo": repository,
                "org": GitHubConfig.organisation,
                "pullRequestCursor": end_cursor
            })

            prs = result["repositoryOwner"]["repository"]["pullRequests"]
            has_next_page = end_cursor = prs["pageInfo"]["endCursor"]

            all_prs.extend(prs["nodes"])

    return all_prs


def issues(repository_names: list[str]) -> list[dict[str, Any]]:
    """
    Run a GraphQL query for all issues in provided repositories.

    This automatically handles any pagination.
    """
    issues = []

    for repository in repository_names:
        has_next_page = True
        end_cursor = None

        while has_next_page:
            result = client.execute(load_query("issues"), variable_values={
                "repo": repository,
                "org": GitHubConfig.organisation,
                "issueCursor": end_cursor
            })

            page_issues = result["repositoryOwner"]["repository"]["issues"]
            has_next_page = end_cursor = page_issues["pageInfo"]["endCursor"]

            issues.extend(page_issues["nodes"])

    return issues


def repos() -> list[str]:
    """Return all repositories on the configured organisation."""
    repos = []

    has_next_page = True
    end_cursor = None

    while has_next_page:
        result = client.execute(load_query("repos"), variable_values={
            "org": GitHubConfig.organisation,
            "repositoryCursor": end_cursor
        })

        repositories = result["repositoryOwner"]["repositories"]
        has_next_page = end_cursor = repositories["pageInfo"]["endCursor"]

        for repo in repositories["nodes"]:
            if not repo["isArchived"]:
                repos.append(repo["name"])

    return repos
