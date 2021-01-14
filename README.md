# A RESTful API using Flask

## Features:
* Sorting given data consisting of an integer list

* Support ordering the sorted list return by api in ASCENDING or DESCENDING 

## Notes
1. Sending POST request with json body include  in the form a list e.g. { [1, 7, 2, 6] } under variable name `data`, and `order` variable which  receive one value between `asc` and `desc` 
2. Response includes the sorted list under name `sorted_data` 
3. This api endpoint limits payload by `2 MB`
4. This api endpoint has rate limit which specified in `configs.yaml`

        
            day: "500 per day"
            hour: "200 per hour"
            second: "20 per second"
        


## Project tructure

    .
    ├── requirements.txt                # Dependent package requirements
    ├── configs.yaml                    # Configuration file
    ├── flask_sorting_service.py        # Source file
    ├── test_services.py                # Test file
    ├── util.py                         # Utilities
    └── README.md


## Install:

pip install -r requirements.txt

## Run (Python 3.6 compatible):
**Serve Flask app back-end :**

cd <path_to_root_folder_of_project>

python flask_sorting_service.py

**API:**

http://\<host>:5000/sorting

Methods: POST

JSON: ex: {"data": [11, 2, 99], "order": 'asc'}

Description: return a sorted list


**Run Functional tests:**

python test_services.py


