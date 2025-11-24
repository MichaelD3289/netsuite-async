# Contributing to netsuite-async

Thank you for your interest in contributing to netsuite-async!

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/netsuite-async.git
   cd netsuite-async
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Code Style

We use **Black** for code formatting. Before submitting changes:

```bash
uv run black src/
```

## Making Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Format your code with Black

4. Update documentation if needed

5. Commit your changes:
   ```bash
   git commit -m "Add feature: description of what you added"
   ```

## Pull Request Process

1. Fork the repository and create your branch from `main`
2. Make your changes and format with Black
3. Update the CHANGELOG.md if needed
4. Submit a pull request with a clear description

## Reporting Issues

When reporting bugs, please include:
- Python version
- netsuite-async version  
- Minimal code example that reproduces the issue
- Full error traceback

For feature requests, describe the use case and why it would be valuable.

## Questions?

Feel free to open an issue for questions.