

# Title: Cintas Address Matching Tool

## Description:

This is a personal project developed to assist my mother in her position at Cintas by efficiently comparing two CSV files – one containing a list of affected companies from a report, and the other containing all the companies Cintas has potentially worked with. The goal of this project is to improve the accuracy and consistency of identifying matching addresses between the two files, overcoming the limitations of the previously used software. She went from being able to retrieve only 6 of the companies to 47 companies using my program!

## Key features:

* Compares addresses from two CSV files and identifies matches.
* Preprocesses addresses to account for variations in formatting and abbreviations, improving the matching accuracy.
* Returns matched companies' names and UCIDs (IDs used by Cintas).
* Provides a user-friendly web interface built with Django for easy usage by non-technical users.

## Technologies used:

* Python: The core language used for the address comparison logic and preprocessing.
* Pandas: A Python library used for efficient data manipulation and analysis of the CSV files.
* Regular Expressions (re): A Python module used for pattern matching and substitutions in the address preprocessing stage.
* Django: A high-level Python web framework used for building the web application, handling user input, and rendering results.
* HTML and CSS: Used for designing and styling the user interface.

**This project aims to provide a more reliable and accurate solution to my mother's specific needs at Cintas, enabling her to identify affected companies more effectively and improve overall productivity. The web application simplifies the process of uploading and comparing CSV files, making it an easy-to-use tool that can be accessed whenever needed.**
