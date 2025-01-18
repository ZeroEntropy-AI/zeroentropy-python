# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import Zeroentropy, AsyncZeroentropy
from zeroentropy.types import (
    QueryTopPagesResponse,
    QueryTopSnippetsResponse,
    QueryTopDocumentsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_top_documents(self, client: Zeroentropy) -> None:
        query = client.queries.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
        )
        assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

    @parametrize
    def test_method_top_documents_with_all_params(self, client: Zeroentropy) -> None:
        query = client.queries.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
            filter={},
            include_metadata=True,
        )
        assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

    @parametrize
    def test_raw_response_top_documents(self, client: Zeroentropy) -> None:
        response = client.queries.with_raw_response.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_top_documents(self, client: Zeroentropy) -> None:
        with client.queries.with_streaming_response.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_top_pages(self, client: Zeroentropy) -> None:
        query = client.queries.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
        )
        assert_matches_type(QueryTopPagesResponse, query, path=["response"])

    @parametrize
    def test_method_top_pages_with_all_params(self, client: Zeroentropy) -> None:
        query = client.queries.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
            filter={},
            include_content=True,
        )
        assert_matches_type(QueryTopPagesResponse, query, path=["response"])

    @parametrize
    def test_raw_response_top_pages(self, client: Zeroentropy) -> None:
        response = client.queries.with_raw_response.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryTopPagesResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_top_pages(self, client: Zeroentropy) -> None:
        with client.queries.with_streaming_response.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryTopPagesResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_top_snippets(self, client: Zeroentropy) -> None:
        query = client.queries.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
        )
        assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

    @parametrize
    def test_method_top_snippets_with_all_params(self, client: Zeroentropy) -> None:
        query = client.queries.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
            filter={},
            precise_responses=True,
        )
        assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

    @parametrize
    def test_raw_response_top_snippets(self, client: Zeroentropy) -> None:
        response = client.queries.with_raw_response.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = response.parse()
        assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

    @parametrize
    def test_streaming_response_top_snippets(self, client: Zeroentropy) -> None:
        with client.queries.with_streaming_response.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = response.parse()
            assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQueries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_top_documents(self, async_client: AsyncZeroentropy) -> None:
        query = await async_client.queries.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
        )
        assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

    @parametrize
    async def test_method_top_documents_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        query = await async_client.queries.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
            filter={},
            include_metadata=True,
        )
        assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_top_documents(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.queries.with_raw_response.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_top_documents(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.queries.with_streaming_response.top_documents(
            collection_name="collection_name",
            k=0,
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryTopDocumentsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_top_pages(self, async_client: AsyncZeroentropy) -> None:
        query = await async_client.queries.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
        )
        assert_matches_type(QueryTopPagesResponse, query, path=["response"])

    @parametrize
    async def test_method_top_pages_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        query = await async_client.queries.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
            filter={},
            include_content=True,
        )
        assert_matches_type(QueryTopPagesResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_top_pages(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.queries.with_raw_response.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryTopPagesResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_top_pages(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.queries.with_streaming_response.top_pages(
            collection_name="collection_name",
            k=0,
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryTopPagesResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_top_snippets(self, async_client: AsyncZeroentropy) -> None:
        query = await async_client.queries.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
        )
        assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

    @parametrize
    async def test_method_top_snippets_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        query = await async_client.queries.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
            filter={},
            precise_responses=True,
        )
        assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

    @parametrize
    async def test_raw_response_top_snippets(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.queries.with_raw_response.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        query = await response.parse()
        assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

    @parametrize
    async def test_streaming_response_top_snippets(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.queries.with_streaming_response.top_snippets(
            collection_name="collection_name",
            k=0,
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            query = await response.parse()
            assert_matches_type(QueryTopSnippetsResponse, query, path=["response"])

        assert cast(Any, response.is_closed) is True
