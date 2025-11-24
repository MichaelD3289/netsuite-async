# async_netsuite/client.pyi

from typing import Any
from netsuite_async.client.accessors import RecordAccessor


class AsyncNetsuiteRestClient:
    # ------------------------------------
    # Static shadow of dynamically-added API
    # ------------------------------------
    projects: RecordAccessor
    contacts: RecordAccessor
    customers: RecordAccessor
    partners: RecordAccessor
    employees: RecordAccessor

    # ------------------------------------
    # Constructor & real methods
    # ------------------------------------
    def __init__(self, account_id: str, http_client: Any, **kwargs) -> None: ...
    def build_url(self, record_name: str, internal_id: str | None = None) -> str: ...
    def __getattr__(self, name: str) -> RecordAccessor: ...
