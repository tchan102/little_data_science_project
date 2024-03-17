# Little Data Science Project

## Project Overview

This project involves scripts that create a panda DataFrame from internship data. The primary source of this data is the [intern repository by Pitt CSC & Simplify](https://github.com/SimplifyJobs/Summer2024-Internships). This project aims to parse and analyze internship listings, extracting valuable insights such as company names, job titles, locations, and application dates.

## Features

- **Data Parsing**: Scripts to parse internship listings from HTML content.
- **Data Analysis**: Analyze the listings to extract insights such as most common locations, companies hiring, etc.
- **Visualization**: Generate visualizations for the analyzed data.
- **CSV Export**: Capability to export parsed data into CSV format for further analysis.

## Files Description

- `InternTable.py`: Python script containing the logic to parse internship listings and generate a DataFrame.
- `main.py`: The main entry point of the project, orchestrating the parsing and analysis.
- `short_script.html`, `table.html`: HTML files used as data sources for the parsing scripts.
- Under the records directory, `2024-03-16.csv`, `2024-03-17.csv`: CSV files containing processed data from the project.

## Setup

1. Ensure you have Python installed on your system.
2. Install required libraries:
    ```bash
    pip install pandas beautifulsoup4 matplotlib
    ```
3. Clone the repository to your local machine.
4. Run the main script:
    ```bash
    python main.py
    ```

## How to Use

- Modify `main.py` to point to the specific HTML or CSV files you wish to parse and analyze.
- Run `main.py` to see the output DataFrame in your console or to export it as a CSV file.

## Contributing

Contributions to this project are welcome! Whether it's adding new features, fixing bugs, or improving documentation, your help is appreciated.

## License

This project is open source, feel free to use it for any legal purpose.
