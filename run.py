from config import SAMPLE_STATUS, INPUT_UNIVARIATE_DATA, INPUT_PAIRED_DATA
from sign_test_small_sample import sign_test_small_sample
from sign_test_large_sample import sign_test_large_sample
from create_table import create_table

import pandas as pd

paired_large_sample_status = SAMPLE_STATUS['large_sample']['paired_sample']
one_large_sample_status = SAMPLE_STATUS['large_sample']['One_sample']
paired_small_sample_status = SAMPLE_STATUS['small_sample']['paired_sample']
one_small_sample_status = SAMPLE_STATUS['small_sample']['One_sample']


if one_small_sample_status:
    print('\n """Results of the Sign Test of a small sample having only one variable""" \n')

    try:
        path_to_csv = INPUT_UNIVARIATE_DATA['small_sample']['csv_file_directory']
        column_name = INPUT_UNIVARIATE_DATA['small_sample']['univariate_case']['one_column']
        median = INPUT_UNIVARIATE_DATA['small_sample']['parameters']['median']
        significance_level = INPUT_UNIVARIATE_DATA['small_sample']['parameters']['alpha']
        alternative = INPUT_UNIVARIATE_DATA['small_sample']['parameters']['alternate']

        if path_to_csv != "" and column_name != "" and median != "" and significance_level != "" and alternative != "":
            data = pd.read_csv(path_to_csv)
            column_data = data[column_name]
            results = sign_test_small_sample(data, column_data, md=median,
                                                                   alpha=significance_level, alternate=alternative)

            file_path = 'Output\Table_large_001.html'

            create_table(results, file_path)

        else:
            print('\n There is a missing value in required keys of INPUT_UNIVARIATE_DATA.')

    except Exception as e:
        error_message = str(e)
        print(error_message)


if paired_small_sample_status:

    print('\n """Results of the Sign Test of a paired Sample with small in size""" \n')

    try:
        path_to_csv = INPUT_PAIRED_DATA['small_sample']['csv_file_directory']
        first_column_name = INPUT_PAIRED_DATA['small_sample']['paired_case']['first_column']
        second_column_name = INPUT_PAIRED_DATA['small_sample']['paired_case']['second_column']
        median = INPUT_PAIRED_DATA['small_sample']['parameters']['median']
        significance_level = INPUT_PAIRED_DATA['small_sample']['parameters']['alpha']
        alternative = INPUT_PAIRED_DATA['small_sample']['parameters']['alternate']

        if path_to_csv != "" and first_column_name != "" and second_column_name != "" and median != "" and significance_level != "" and alternative != "":
            data = pd.read_csv(path_to_csv)
            column_1_data = data[first_column_name]
            column_2_data = data[second_column_name]
            new_column_name = 'difference (' + second_column_name + '-' + first_column_name + ')'
            data[new_column_name] = column_2_data - column_1_data
            column_data = data[new_column_name]
            results = sign_test_small_sample(data, column_data, md=median,
                                                                   alpha=significance_level, alternate=alternative)

            file_path = 'Output\Table_large_002.html'

            create_table(results, file_path)

        else:
            print('\n There is a missing value in required keys of INPUT_PAIRED_DATA.')

    except Exception as e:
        error_message = str(e)
        print(error_message)


if one_large_sample_status:
    print('\n """Results of the Sign Test of a large sample with only one variable"""')

    try:
        path_to_csv = INPUT_UNIVARIATE_DATA['large_sample']['csv_file_directory']
        column_name = INPUT_UNIVARIATE_DATA['large_sample']['univariate_case']['one_column']
        median = INPUT_UNIVARIATE_DATA['large_sample']['parameters']['median']
        significance_level = INPUT_UNIVARIATE_DATA['large_sample']['parameters']['alpha']
        alternative = INPUT_UNIVARIATE_DATA['large_sample']['parameters']['alternate']

        if path_to_csv != "" and column_name != "" and median != "" and significance_level != "" and alternative != "":
            data = pd.read_csv(path_to_csv)
            column_data = data[column_name]
            results = sign_test_large_sample(data, column_data, md=median, alpha=significance_level,
                                             alternate=alternative)

            file_path = 'Output\Table_large_003.html'

            create_table(results, file_path)

        else:
            print('\n There is a missing value in required keys of INPUT_UNIVARIATE_DATA.')

    except Exception as e:
        error_message = str(e)
        print(error_message)

if paired_large_sample_status:
    print('\n """Results of the Sign Test of a paired Sample with large in size"""')

    try:
        path_to_csv = INPUT_PAIRED_DATA['large_sample']['csv_file_directory']
        first_column_name = INPUT_PAIRED_DATA['large_sample']['paired_case']['first_column']
        second_column_name = INPUT_PAIRED_DATA['large_sample']['paired_case']['second_column']
        median = INPUT_PAIRED_DATA['large_sample']['parameters']['median']
        significance_level = INPUT_PAIRED_DATA['large_sample']['parameters']['alpha']
        alternative = INPUT_PAIRED_DATA['large_sample']['parameters']['alternate']

        if path_to_csv != "" and first_column_name != "" and second_column_name != "" and median != "" and significance_level != "" and alternative != "":
            data = pd.read_csv(path_to_csv)
            column_1_data = data[first_column_name]
            column_2_data = data[second_column_name]
            new_column_name = 'difference (' + second_column_name + '-' + first_column_name + ')'
            data[new_column_name] = column_2_data - column_1_data
            column_data = data[new_column_name]
            results = sign_test_large_sample(data, column_data, md=median, alpha=significance_level,
                                             alternate=alternative)

            file_path = 'Output\Table_large_004.html'

            create_table(results, file_path)

        else:
            print('\n There is a missing value in required keys of INPUT_PAIRED_DATA.')

    except Exception as e:
        error_message = str(e)
        print(error_message)
