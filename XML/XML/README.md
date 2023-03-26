# XML and Python Assignment
This project contains an XML document and Python scripts that demonstrate how to validate the document against an XML schema and a DTD.

## Files
movies.xml: An example XML document that we will validate against the schema and DTD.
DTD.xsd: An XML schema that defines the structure and content of the example.xml document.
dom_parser.py: A Python script that parses and validates the example.xml document against the example_schema.xsd schema using the Python xmlschema library.
example.dtd: A DTD that defines the structure and content of the example.xml document.
dom_parser_dtd.py: A Python script that parses and validates the example.xml document against the example.dtd DTD using the Python xml.dom.pulldom library.
## Usage
To validate the example.xml document against the XML schema, run the following command:


``python dom_parser.py``
If the validation is successful, the script will output a message indicating that the document is valid against the schema. If the validation fails, the script will output an error message.

## To validate the movies.xml document against the DTD, run the following command:


``python dom_parser_dtd.py``
If the validation is successful, the script will output a message indicating that the document is valid against the DTD. If the validation fails, the script will output an error message.

## Requirements
To run the Python scripts, you must have Python 3.x installed on your system. Additionally, the xmlschema and xml.dom.pulldom libraries are used for schema and DTD validation, respectively. If you do not have these libraries installed, you can install them using pip by running the following commands:

``
pip install xmlschema
pip install xml.dom.pulldom
``
## License
This project is licensed under the MIT License. See the LICENSE file for details.