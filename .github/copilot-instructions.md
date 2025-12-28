# AI Coding Agent Instructions for the Engine Project

## Overview
The Engine project is a Python-based framework designed for modular game development. It is structured to support core functionalities like game loops, rendering, and module management. The project is distributed as a Python package and adheres to the MIT license.

## Architecture
The codebase is organized into the following major components:

- **Core**: Contains the foundational logic for the engine, including the game loop and module management.
  - Example: `src/engine/core/game.py`
- **Modules**: Implements modular functionalities like loaders, renderers, and other utilities.
  - Example: `src/engine/core/modules/`
- **Renderer**: Handles rendering logic, including window management and drawing operations.
  - Example: `src/engine/core/modules/renderer/`
- **Tests**: Contains unit tests for validating the functionality of the engine.
  - Example: `tests/`

## Developer Workflows

### Running Tests
To run the test suite, use the following command:
```bash
pytest tests/
```

### Debugging
Use Python's built-in debugging tools like `pdb` or external tools like `debugpy` for debugging. Place breakpoints in the relevant files to inspect runtime behavior.

### Building and Installing
To build and install the package locally:
```bash
pip install .
```

## Project-Specific Conventions

- **Modular Design**: Each module in `src/engine/core/modules/` should be self-contained and follow the single-responsibility principle.
- **Testing**: Tests are organized to mirror the structure of the `src/` directory. For example, tests for `loader.py` are in `tests/module.py`.
- **Documentation**: All public functions and classes should include docstrings following the Google Python Style Guide.

## Integration Points

- **External Dependencies**: The project relies on `pytest` for testing and `pip` for package management.
- **Cross-Component Communication**: Modules communicate through well-defined interfaces. For example, the game loop interacts with the renderer via the `renderer` module.

## Examples

### Adding a New Module
1. Create a new Python file in `src/engine/core/modules/`.
2. Implement the module's functionality.
3. Add tests for the module in the `tests/` directory.

### Modifying the Game Loop
1. Edit `src/engine/core/game.py`.
2. Ensure changes are backward-compatible.
3. Update relevant tests in `tests/`.

## Key Files
- `src/engine/core/game.py`: Main game loop logic.
- `src/engine/core/modules/renderer/`: Rendering logic.
- `tests/`: Unit tests.

## License
This project is licensed under the MIT License. See `LICENSE.txt` for details.