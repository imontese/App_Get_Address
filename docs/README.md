# Etherscan Address Analyzer  
  
This project consists of two Python files, `get_address.py` and `main.py`, which are used to analyze Ethereum addresses and their associated holdings based on data from Etherscan.io. The project also includes a simple graphical user interface (GUI) built using PyQt6.  

1. Data Collection: The address analysis logic reads Ethereum address data from a CSV file, which should be in the format exported from Etherscan.- io. The data includes the date and time of transactions, the destination addresses, and the quantity of holdings.
2. Data Processing: The logic processes the collected data by sorting and filtering the addresses based on the quantity of holdings. It removes duplicate addresses and retains only the ones with the highest value.
3. Address Balance Scraping: For each address, the logic scrapes the balance using the BeautifulSoup library. It sends an HTTP request to Etherscan.io, parses the HTML response, and extracts the balance information.
4. Address Balance Comparison: The balance of each address is compared with a user-specified threshold. If the balance is greater than the threshold, the address is considered significant and saved to a text file.
5. GUI Interaction: The main.py file contains the code for the PyQt6 GUI, which allows users to interact with the application. Users can start the address analysis process, close the application, and open the output file containing the significant addresses.
  
## Files  
  
### get_address.py  
  
This file contains the main logic for scraping and analyzing Ethereum addresses. It performs the following tasks:  
  
1. Read address data from a CSV file.  
2. Filter and sort the addresses based on the quantity of holdings.  
3. Scrape the balance of each address using BeautifulSoup.  
4. Compare the balance of each address with a specified threshold.  
5. Save the addresses with a balance greater than the threshold to a text file.  
  
### main.py  
  
This file contains the code for the PyQt6 GUI. It allows the user to:  
  
1. Start the address analysis process.  
2. Close the application.  
3. Open the output file containing the addresses with a balance greater than the threshold.  
  
## Usage  
  
1. Install the required packages using pip:  
  
```bash  
pip install -r requirements.txt  
 
2. Run the main.py file:
python main.py  
 
3. Use the GUI to start the address analysis process and view the results.
Dependencies
 

Python 3.6 or later
BeautifulSoup
pandas
numpy
PyQt6
qdarkstyle
requests
re
time
warnings
  
Make sure to create a `requirements.txt` file with the necessary packages and their versions for easy installation.