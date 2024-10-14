# Color Catalog

Color Catalog is a simple desktop application that displays a catalog of colors with their names, hex codes, sizes, and SKUs. It allows users to easily view and copy color information.

## Features

- Display color information in a table format
- Show color swatches for each entry
- Copy hex codes and SKUs with right-click context menu
- Scrollable interface for large color catalogs

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)
- pyperclip

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required packages:

```
pip install pyperclip
```

3. Place your color data in a CSV file named `bc3001-skus.csv` in the same directory as the script.

## Usage

1. Run the script:

```
python color_catalog.py
```

2. The application window will open, displaying the color catalog.
3. Scroll through the list to view all colors.
4. Right-click on any row to copy the hex code or SKU.

## CSV File Format

The `bc3001-skus.csv` file should have the following columns:

- Color: The name of the color
- HexCode: The hexadecimal color code
- Size: The size information
- SKU: The stock keeping unit

## Customization

You can modify the column widths by adjusting the `width` parameter in the `tree.column()` calls.

## License

[Include your chosen license here]

## Contributing

[Include guidelines for contributing to the project, if applicable]

## Support

[Include information on how users can get support or report issues]
