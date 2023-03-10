# OSINT-x-CURP

This tool retrieves data from the CURP RENAPO API, a mexican goverment dependency which deals with mexican citizens identity docs, This script is one of the few OSINT tools non-USA focused in order to retrieve and verify data in the OSINT investigations context. Uses python's requests library and a config.json file containing your API keys managed by CURP RENAPO managed RapidAPI.com, points of data obtained aid to validate a mexican citizen identity for OSINT research purposes applied to Missing Persons cases, Fraud prevention and Identity theft investigations.

## Prerequisites

Python 3.x
requests library (pip3 install requests)
A valid suscrisption to CURP RENAPO and its API key.

## Installation

Clone this repository to your local machine.
Install the requests library by running pip install requests in your terminal.

## Configuration

Open the config.json file in the root directory of the repository.
Replace "your_api_key_here" with your actual CURP RENAPO's RapidAPI key.


## Usage

In your terminal, navigate to the root directory of the repository.
Run the following command: 

python3 OSINT-x-CURP.py -h

		      .~~~~`\~~\        
		     ;       ~~ \       
		     |           ;      
		 ,--------,______|---.  
		/          \-----`    \ 
		`.__________`-_______-' 
		 O S I N T  x  C U R P  

		usage: OSINT-x-CURP.py [-h] curp

		Retrieve data from Mexico's CURP RENAPO API

		positional arguments:
		  curp        The CURP to retrieve

		options:
		  -h, --help  show this help message and exit


The script will send a GET request to the CURP API using the specified CURP and your RapidAPI key from the config.json file.
If the request is successful, the script will print the data returned by the API. Otherwise, it will print an error message with the status code.
This will send a GET request to the CURP API with your RapidAPI key and print the data returned by the API in json format. The points of data retrieved are the following: birthdate, curp, entity_birth, homonimo, mothers_maiden_name, names, nationality, paternal_surname, probation_document, probation_document_data, anioReg, crip, cveEntidadEmisora, cveMunicipioReg, foja, folioCarta, libro, numActa, numEntidadReg, numRegExtranjeros, tomo': renapo_valid, sex, status_curp, RCN and transaction_id.
