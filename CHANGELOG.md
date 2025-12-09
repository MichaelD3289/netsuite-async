# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- N/A

### Changed

- N/A

### Deprecated

- N/A

### Removed

- N/A

### Fixed

- N/A

### Security

- N/A

## [0.1.4] - 2025-12-09

### Removed

- "Prefer: transient" header as it's only relevant for SuiteQL queries, not REST record operations

## [0.1.3] - 2025-12-03

### Fixed

- Environment variable validation no longer occurs on import, allowing library usage without env vars when providing explicit credentials
- Type stub file to match updated AsyncNetsuiteRestClient constructor signature

## [0.1.2] - 2025-12-01

### Added

- Automated PyPI deployment workflow via GitHub Actions

### Fixed

- Type stub file (rest.pyi) to match current AsyncNetsuiteRestClient implementation

## [0.1.1] - 2025-11-24

### Removed

- Unused pydantic and pydantic-settings dependencies for smaller package size

## [0.1.0] - 2025-11-24

### Added

- Initial release of netsuite-async
- Async-first NetSuite REST API client with AsyncAuthProvider pattern
- OAuth 1.0 authentication with HMAC-SHA256 signatures
- OAuth1AsyncAuthProvider for simplified authentication setup
- RecordAccessor with comprehensive CRUD operations:
  - `get()` and `get_many()` for individual and bulk record fetching
  - `all_full()` and `all_full_concurrent()` for complete dataset retrieval
  - `list_summaries()` and `list_summaries_concurrent()` for pagination
  - `iter_summary_pages()` for memory-efficient streaming
  - `create()` and `update()` for record mutations
- Concurrent operations with configurable limits and semaphore-based rate limiting
- Smart pagination (sequential and concurrent strategies)
- RecordCatalog for record type mapping with built-in common types
- Comprehensive error handling with typed exception hierarchy
- Dynamic record access with fuzzy matching for typos
- Type-safe data models (FullRecord, SummaryRecord, FetchResult) with full type hints
- Comprehensive docstrings with examples for all public methods
- Complete API reference and performance guidance
- Context manager support for automatic resource cleanup
