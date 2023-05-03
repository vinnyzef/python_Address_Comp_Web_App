import pandas as pd
import re


class CompareForms:
    def __init__(self, csv1, csv2):
        self.csv1 = csv1
        self.csv2 = csv2

    def preprocess_address(self, address):
        # Convert non-string values to strings
        address = str(address)

        # Convert to lowercase
        address = address.lower()

        # Replace common abbreviations and variations using regex
        abbreviations = [
            (r'\b(st)\b\.?', 'street'),
            (r'\b(ave)\b\.?', 'avenue'),
            (r'\b(rd)\b\.?', 'road'),
            (r'\b(blvd)\b\.?', 'boulevard'),
            (r'\b(drv)\b\.?', 'drive'),
            (r'\b(ct)\b\.?', 'court'),
            (r'\b(pl)\b\.?', 'place'),
            (r'\b(ln)\b\.?', 'lane'),
            (r'\b(pkwy)\b\.?', 'parkway'),
            (r'\b(expy)\b\.?', 'expressway'),
            (r'\b(hwy)\b\.?', 'highway'),
            (r'\b(ste)\b\.?', 'suite'),
            (r'\b(unit)\b', 'suite'),
            (r'\b(rm)\b\.?', 'suite'),
            (r'\b(apt)\b\.?', 'suite'),
            (r'\b(bldg)\b\.?', 'suite'),
            (r'\b(fl)\b\.?', 'floor'),
        ]

        for pattern, replacement in abbreviations:
            address = re.sub(pattern, replacement, address)

        # Compass directions
        address = re.sub(r'\b(ne)\b', 'northeast', address)
        address = re.sub(r'\b(nw)\b', 'northwest', address)
        address = re.sub(r'\b(se)\b', 'southeast', address)
        address = re.sub(r'\b(sw)\b', 'southwest', address)
        address = re.sub(r'\b(e)\b', 'east', address)
        address = re.sub(r'\b(w)\b', 'west', address)
        address = re.sub(r'\b(n)\b', 'north', address)
        address = re.sub(r'\b(s)\b', 'south', address)

        # Remove '#' from suite numbers
        address = address.replace('#', '')

        # Remove extra whitespace
        address = ' '.join(address.split())

        return address

    def compare(self):
        # Read the CSV files
        table1 = pd.read_csv(self.csv1)
        table2 = pd.read_csv(self.csv2)
        # Preprocess addresses
        table1['Address 1'] = table1['Address 1'].apply(
            self.preprocess_address)
        table2['Address'] = table2['Address'].apply(self.preprocess_address)

        # Create an empty result DataFrame
        result = pd.DataFrame(columns=['Name 1', 'UCID'])

        for index, row in table2.iterrows():
            # Check if the address exists anywhere in the "Address 1" column of file 1
            matching_rows = table1[table1['Address 1'] == row['Address']]

            if not matching_rows.empty:
                name1 = matching_rows.iloc[0]['Name 1']
                if name1 not in result['Name 1'].values:
                    matched_data = pd.DataFrame(
                        {'Name 1': [name1], 'UCID': [row['UCID']]})
                    result = pd.concat(
                        [result, matched_data], ignore_index=True)
        # Print the result
        return result.to_string(index=False)


# # Example usage:
# compare = CompareForms('path/to/csv1.csv', 'path/to/csv2.csv')
# compare.compare()
