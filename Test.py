
property_database = {
    "Property 1": [
        "Cali 1",
        "0x507BFb01f2F2e73f428C197bF3059AaC8ef73caf",
        "1000",
        0.50,
        "Images/california_beach2.jpeg",
    ],
    "Property 2": [
        "Cali 2",
        "0x0cfCfac45FEcEcbCAF8Fb78D257041Cbb7F6Ca41",
        "1500",
        1.00,
        "Images/california_beach3.jpeg",
    ],
    "Property 3": [
        "Cali 3",
        "0x58AcEf7b776A19Eb5536f5c7D189c73bbaF6d313",
        "2000",
        1.50,
        "Images/california_beach4.jpeg",
    ]
}

# A list of the Properties
property = ["Cali 1", "Cali 2", "Cali 3"]

cali = property_database["Property 3"][3]
print(cali)