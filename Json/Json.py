import json
import sys


data =""" {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}"""


print(type(data))
data_n = json.loads(data)
json.dumps(data_n)
print(type(data_n))


