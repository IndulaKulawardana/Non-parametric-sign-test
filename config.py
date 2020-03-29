SAMPLE_STATUS = {
    "small_sample": {
        "One_sample": True,
        "paired_sample": True
    },
    "large_sample": {
        "One_sample": True,
        "paired_sample": False,
    }
}


INPUT_UNIVARIATE_DATA = {
    "small_sample": {
        "csv_file_directory": "Input/sample_1.csv",
        "univariate_case": {
            "one_column": "Number of customer per day",
        },
        "parameters": {
            "median": 750,
            "alpha": 5,
            "alternate": "greater than"
        }
    },
    "large_sample": {
        "csv_file_directory": "Input/sample_2.csv",
        "univariate_case": {
            "one_column": "Sales"
        },
        "parameters": {
            "median": 5120,
            "alpha": 5,
            "alternate": "less than"
        }
    }

}


INPUT_PAIRED_DATA = {
    "small_sample": {
        "csv_file_directory": "Input/sample_3.csv",
        "paired_case": {
            "first_column": "Mean score before class",
            "second_column": "Mean score after class"
        },
        "parameters": {
            "median": 0,
            "alpha": 5,
            "alternate": "greater than"
        }
    },
    "large_sample": {
        "csv_file_directory": "",
        "paired_case": {
            "first_column": "",
            "second_column": ""
        },
        "parameters": {
            "median": "",
            "alpha": "",
            "alternate": ""
        }
    }
}






