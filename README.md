# Wikipedia Birth Article Search Script

This simple script interacts with the Wikipedia API to retrieve information about articles published on the Portuguese Wikipedia site related to specific birth dates. It uses the `pandas` and `wikipedia` libraries for data manipulation and Wikipedia API interaction.

## Usage

1. Ensure you have the required libraries installed:

```bash
pip install pandas wikipedia-api
```

2. **Example Data Files:**
   - Create a CSV file named `data.csv` with the following columns: `Id`, `Name`, and `Birth`. Each row should represent an individual with a unique identifier (`Id`), name (`Name`), and birth date (`Birth`) in the format dd/mm/yyyy. An example of this file's structure is provided in `data.csv`.

3. Run the script in your Python environment:

```bash
python wiki-birth.py
```

4. Follow the prompts to input your birth date in the format dd/mm/yyyy.
5. The script will display the title of an article published on the Portuguese Wikipedia site that is related to the provided birth date. It will also provide a link to the full article in the terminal.

6. A new CSV file named `new_data.csv` will be generated. This file will contain updated information, including article titles, URLs, and summaries related to the birth dates. An example of this file's structure is provided in `new_data.csv`.

## Script Overview

1. The script starts by importing the necessary libraries: `pandas` as `pd` and `wikipedia` as `wp`.

2. It prompts the user to input their birth date.

3. The Wikipedia language is set to Portuguese using `wp.set_lang("pt")`.

4. The script reads data from `data.csv` into a `pandas` DataFrame.

5. Lists are created to store article information: `ids`, `names`, `births`, `titles`, `urls`, and `summarys`.

6. The user's birth date is used to search for related Wikipedia articles, and the title and URL of the first article are retrieved and stored.

7. The function `search_article` is defined to search for articles based on birth dates. It returns article information if found; otherwise, it returns default values.

8. The script iterates through the data, searches for articles related to each individual's birth date, and appends article information to the respective lists.

9. A list of dictionaries containing individual information is created.

10. A new `pandas` DataFrame is generated using the list of dictionaries, and the data is saved to a CSV file named `new_data.csv`.

## Note

- The script assumes that the `wikipedia` library can successfully retrieve articles using the provided birth dates.

- Ensure that the input data in `data.csv` follows the specified structure.

- Exercise caution when interacting with external APIs and adhere to their usage policies and limits.

- Example data files (`data.csv` and `new_data.csv`) are provided to illustrate the expected format of the input and output files.

Feel free to adapt the script to your needs and requirements.
