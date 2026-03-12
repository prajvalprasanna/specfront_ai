# Techfront AI: Pip Packaging & Distribution Guide

This guide outlines exactly how to build and package `techfront_ai` as a proper pip package and distribute it via PyPI.

## Prerequisites

Ensure you have the latest versions of build tools installed:

```bash
python -m pip install --upgrade pip
pip install build twine
```

## Step 1: Building the Package

To generate the distribution archives (the `.whl` and `.tar.gz` files), run the following command from the root directory that contains `pyproject.toml`:

```bash
python -m build
```

The output will be placed in a newly created `dist/` directory. You should see two files, similar to:
- `dist/techfront_ai-0.1.0-py3-none-any.whl` (Built Distribution)
- `dist/techfront_ai-0.1.0.tar.gz` (Source Distribution)

## Step 2: Local Testing (Optional but Recommended)

Before publishing, it's heavily recommended to test the package locally. Create a fresh virtual environment:

```bash
python -m venv test_env
# Windows:
test_env\Scripts\activate
# macOS/Linux:
source test_env/bin/activate

# Install the built wheel
pip install dist/techfront_ai-0.1.0-py3-none-any.whl
```

Once installed, verify the CLI works:
```bash
techfront_ai --help
techfront_ai init
techfront_ai mcp
```

## Step 3: Publishing to PyPI

When you are ready to publish, use `twine` to upload the archives securely. 

### Publish to TestPyPI (Dry Run)
It's a good practice to upload to the PyPI testing server first:
```bash
twine upload --repository testpypi dist/*
```

### Publish to Official PyPI (Production)
Once verified, upload to the actual Python Package Index:
```bash
twine upload dist/*
```

You will be prompted to enter your PyPI username and password (or an API token, prefixed with `__token__`).

## Step 4: Distribution & Usage

After successful publication, any developer around the world can install the agent integration into their workspace instantly:

```bash
pip install specfront_ai
specfront_ai init
```

## Step 5: Updating the Package (Development Workflow)

Since you are in active development, you will likely need to push updates frequently. PyPI requires a unique version number for every successful upload.

When you want to release a new version:

1. **Increment the Version**: Open `pyproject.toml` and change the `version` string (e.g., from `"0.1.0"` to `"0.1.1"`).
2. **Clean Old Builds (Optional)**: Delete the `dist/` directory to avoid confusion with older versions.
   ```bash
   # Windows
   rmdir /S /Q dist
   # macOS/Linux
   rm -rf dist/
   ```
3. **Rebuild**: Generate the new distribution archives.
   ```bash
   python -m build
   ```
4. **Publish**: Upload the newly built archives to PyPI.
   ```bash
   twine upload dist/*
   ```

*Tip users will need to run `pip install --upgrade specfront_ai` to pull your latest changes!*
