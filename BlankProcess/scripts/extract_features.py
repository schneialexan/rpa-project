import requests

def process_with_olama(data):
    headers = {
                "Content-Type": "application/json"
                }
    
    prompt = """Return a JSON-Object with the following Form and Values:
    {'Invoicenumber': Invoicenumber (Format: String),
    'FirstName': First Name (Invoicereceiver) (Format: String),
    'LastName': Last Name (Invoicereceiver) (Format: String),
    'Address': Address (Invoicereceiver) (Format: String),
    'Amount': Invoice Amount (Total) (Format: Decimal),
    'Company': Company Name (Format: String),
    'InvoiceDate': Invoice Date (Format: yyyy-MM-dd)
    }
    Do not change anything on the structure and only return the JSON without explanation or starting sentences!\n\nHere is the Data:\n\n\n"""+data
    
    json_data = {
                    "model": "llama3:latest",
                    "prompt": prompt,
                    "stream": False
                 }
    
    response = requests.post("http://localhost:11434/api/generate", 
                             headers = headers,
                             json = json_data
                             )
    
    return response.json()['response']

if __name__ == "__main__":
    data = "Hello, Ollama are you there?!"
    result = process_with_olama(data)
    print(result)