this is my in house library for interacting with Zimra's FDMS system 
# Fiscal Device Management System (FDMS) API Client

This repository provides a Python client for interacting with the Fiscal Device Gateway API (aka FDMS) provided by ZIMRA. The client can be used to manage various operations related to fiscal devices, such as registering a device, fetching configurations, issuing certificates, and handling fiscal day operations.

PLEASE NOTE THAT THE FDMS IS A STATEFUL SYSTEM, SO YOU NEED TO KEEP TRACK OF THE FISCAL DAY NUMBER AND THE RECEIPT COUNTERS. THE CLIENT DOES NOT KEEP TRACK OF THESE FOR YOU



## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Class Methods](#class-methods)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this client, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/gnzima/zimra-public.git
cd zimra-public
pip install -r requirements.txt
```

Or you can just pip install from pypi

```bash
pip install zimra
```

## Usage

You can use the `Device` class to interact with the Fiscal Device Gateway API. Below is an example of how to initialize the class and perform some operations.

### Example

```python
from zimra import Device

# Initialize the device in test mode
device = Device(
    device_id: str, 
    serialNo: str, 
    activationKey: str, 
    cert_path: str, 
    private_key_path:str, 
    test_mode:bool =True, 
    deviceModelName: str='Model123', 
    deviceModelVersion:str = '1.0',
    company_name:str ="Nexus"
)

# Open a fiscal day
fiscal_day_status = device.openDay(fiscalDayNo=102)
print(fiscal_day_status)
```


```python
# Submit a receipt
example_invoice = {
  "deviceID": 12345,
  "receiptType": "FISCALINVOICE",
  "receiptCurrency": "USD",
  "receiptCounter": 1,
  "receiptGlobalNo": 1,
  "invoiceNo": "mz-1",
  "receiptDate": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'), #example: "2021-09-30T12:00:00",
  "receiptLines": [
    {"item_name": "0percent_item",
      "tax_percent": 0.00,
      "quantity": 1,
      "unit_price": 10.00
    },
    {"item_name": "15percent_item2",
      "tax_percent": 15.00,
      "quantity": 1,
      "unit_price": 20.00
    }
  ],
  "receiptPayments":[{
    "moneyTypeCode": 0,
    "paymentAmount": 30.00
    }]
}

receipt = device.prepareReceipt(example_invoice) # this method does all the heavy lifting for you

receipt_status = device.submitReceipt(receipt) # this method submits the receipt to the fiscal device management system and if the receipt has no errors, a QR url is returned which can be used to make the qr code to be printed on receipt, otherwise it returns the error message
print(receipt_status)
```

## Class Methods

### `__init__(self, test_mode=False, *args)`

Initializes the Device class. 

- `test_mode`: Boolean to specify whether to use the test environment or production environment.

### `register(self)`

Registers the device.

### `getConfig(self)`

Fetches the device configuration and updates the device attributes.

### `issueCertificate(self)`

Issues a certificate for the device.

### `getStatus(self)`

Gets the current status of the device.

### `openDay(self, fiscalDayNo, fiscalDayOpened=None)`

Opens a fiscal day.

### `prepareReceipt(self, receiptData)`

Prepares a receipt to be submitted to the fiscal device management system.
It calculates the taxes and formats them in the required format
It signs the receipt as well using the private key provided

### `submitReceipt(self, receiptData)`

Submits a receipt to the fiscal device gateway.

### `closeDay(self)`

Closes the fiscal day. 
It also creates the fiscal day signature based on all the day's transactions

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
This project is still in development and there are many features that can be added to make work simpler for front end developers

## License

This project is licensed under the MIT License. See the LICENSE file for details.
