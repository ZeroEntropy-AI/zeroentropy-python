# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import Zeroentropy, AsyncZeroentropy
from zeroentropy.types import (
    DocumentAddResponse,
    DocumentDeleteResponse,
    DocumentGetInfoResponse,
    DocumentGetInfoListResponse,
    DocumentGetPageInfoResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Zeroentropy) -> None:
        document = client.documents.delete(
            collection_name="collection_name",
            path="path",
        )
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Zeroentropy) -> None:
        response = client.documents.with_raw_response.delete(
            collection_name="collection_name",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Zeroentropy) -> None:
        with client.documents.with_streaming_response.delete(
            collection_name="collection_name",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentDeleteResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: Zeroentropy) -> None:
        document = client.documents.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
        )
        assert_matches_type(DocumentAddResponse, document, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: Zeroentropy) -> None:
        document = client.documents.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
            metadata={"foo": "string"},
            overwrite=True,
        )
        assert_matches_type(DocumentAddResponse, document, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: Zeroentropy) -> None:
        response = client.documents.with_raw_response.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentAddResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: Zeroentropy) -> None:
        with client.documents.with_streaming_response.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentAddResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_info(self, client: Zeroentropy) -> None:
        document = client.documents.get_info(
            collection_name="collection_name",
            path="path",
        )
        assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

    @parametrize
    def test_method_get_info_with_all_params(self, client: Zeroentropy) -> None:
        document = client.documents.get_info(
            collection_name="collection_name",
            path="path",
            include_content=True,
        )
        assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

    @parametrize
    def test_raw_response_get_info(self, client: Zeroentropy) -> None:
        response = client.documents.with_raw_response.get_info(
            collection_name="collection_name",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_get_info(self, client: Zeroentropy) -> None:
        with client.documents.with_streaming_response.get_info(
            collection_name="collection_name",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_info_list(self, client: Zeroentropy) -> None:
        document = client.documents.get_info_list(
            collection_name="collection_name",
        )
        assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

    @parametrize
    def test_method_get_info_list_with_all_params(self, client: Zeroentropy) -> None:
        document = client.documents.get_info_list(
            collection_name="collection_name",
            id_gt="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_get_info_list(self, client: Zeroentropy) -> None:
        response = client.documents.with_raw_response.get_info_list(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_get_info_list(self, client: Zeroentropy) -> None:
        with client.documents.with_streaming_response.get_info_list(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_page_info(self, client: Zeroentropy) -> None:
        document = client.documents.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
        )
        assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

    @parametrize
    def test_method_get_page_info_with_all_params(self, client: Zeroentropy) -> None:
        document = client.documents.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
            include_content=True,
            include_image=True,
        )
        assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

    @parametrize
    def test_raw_response_get_page_info(self, client: Zeroentropy) -> None:
        response = client.documents.with_raw_response.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_get_page_info(self, client: Zeroentropy) -> None:
        with client.documents.with_streaming_response.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.delete(
            collection_name="collection_name",
            path="path",
        )
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.documents.with_raw_response.delete(
            collection_name="collection_name",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.documents.with_streaming_response.delete(
            collection_name="collection_name",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentDeleteResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
        )
        assert_matches_type(DocumentAddResponse, document, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
            metadata={"foo": "string"},
            overwrite=True,
        )
        assert_matches_type(DocumentAddResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.documents.with_raw_response.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentAddResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.documents.with_streaming_response.add(
            collection_name="collection_name",
            content={
                "text": "text",
                "type": "text",
            },
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentAddResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_info(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.get_info(
            collection_name="collection_name",
            path="path",
        )
        assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

    @parametrize
    async def test_method_get_info_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.get_info(
            collection_name="collection_name",
            path="path",
            include_content=True,
        )
        assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_get_info(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.documents.with_raw_response.get_info(
            collection_name="collection_name",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_get_info(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.documents.with_streaming_response.get_info(
            collection_name="collection_name",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetInfoResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_info_list(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.get_info_list(
            collection_name="collection_name",
        )
        assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

    @parametrize
    async def test_method_get_info_list_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.get_info_list(
            collection_name="collection_name",
            id_gt="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
        )
        assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_get_info_list(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.documents.with_raw_response.get_info_list(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_get_info_list(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.documents.with_streaming_response.get_info_list(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetInfoListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_page_info(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
        )
        assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

    @parametrize
    async def test_method_get_page_info_with_all_params(self, async_client: AsyncZeroentropy) -> None:
        document = await async_client.documents.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
            include_content=True,
            include_image=True,
        )
        assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_get_page_info(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.documents.with_raw_response.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_get_page_info(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.documents.with_streaming_response.get_page_info(
            collection_name="collection_name",
            page_index=0,
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGetPageInfoResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True
