import pandas as pd

sign_table_one_sided = pd.read_csv('sign_test_table(one-sided).csv')
sign_table_two_sided = pd.read_csv('sign_test_table(two-sided).csv')


def five_fifty_sample_cal(sample_info, md, alpha, alternate, results):
    if alternate == 'not equal':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is not equal to ' + str(md))

        """Calculation test statistic"""

        test_statistic = min(sample_info['count_minus_sign'], sample_info['count_plus_sign'])
        a = alpha * 2
        critical_value = sign_table_two_sided.iloc[(sample_info['sample_size'] - 1), 1]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'greater than':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is greater than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_minus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 1]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'less than':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is less than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_plus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 1]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    else:
        print("Unknown Type")
        return results


def six_fifty_sample_cal(sample_info, md, alpha, alternate, results):
    if alternate == 'not equal':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is not equal to ' + str(md))

        """Calculation test statistic"""

        test_statistic = min(sample_info['count_minus_sign'], sample_info['count_plus_sign'])
        a = alpha * 2
        critical_value = sign_table_two_sided.iloc[(sample_info['sample_size'] - 1), 2]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'greater than':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is greater than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_minus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 2]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'less than':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is less than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_plus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 2]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    else:

        print("Unknown Type")
        return results


def seven_fifty_sample_cal(sample_info, md, alpha, alternate, results):
    if alternate == 'not equal':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is not equal to ' + str(md))

        """Calculation test statistic"""

        test_statistic = min(sample_info['count_minus_sign'], sample_info['count_plus_sign'])
        a = alpha * 2
        critical_value = sign_table_two_sided.iloc[(sample_info['sample_size'] - 1), 3]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'greater than':

        print('\n Hypothesis')
        print('\n Null Hypothesis:m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is greater than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_minus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 3]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}
        print('\n', results)

        return results

    elif alternate == 'less than':

        print('\n Hypothesis')
        print('\n Null Hypothesis:m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is less than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_plus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 3]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}
        print('\n', results)

        return results

    else:
        print("Unknown Type")
        return results


def eight_fifty_sample_cal(sample_info, md, alpha, alternate, results):
    if alternate == 'not equal':

        print('\n Hypothesis')
        print('\n Null Hypothesis:m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is not equal to ' + str(md))

        """Calculation test statistic"""

        test_statistic = min(sample_info['count_minus_sign'], sample_info['count_plus_sign'])
        a = alpha * 2
        critical_value = sign_table_two_sided.iloc[(sample_info['sample_size'] - 1), 4]

        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'greater than':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is greater than' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_minus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 4]
        print('\n Rejection Criteria: Reject Null Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    elif alternate == 'less than':

        print('\n Hypothesis')
        print('\n Null Hypothesis: m is equal to ' + str(md))
        print('\n Alternative Hypothesis: m is less than ' + str(md))

        """Calculation test statistic"""

        test_statistic = sample_info['count_plus_sign']
        a = alpha
        critical_value = sign_table_one_sided.iloc[(sample_info['sample_size'] - 1), 4]

        print('\n Rejection Criteria: Reject null_Hypothesis at ' + str(a) + '% level of significance ' \
                                                                             'if the test statistic is less than or equal to critical value.')

        column = sample_info['column_data']

        results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                   'Critical Value': critical_value}

        return results

    else:
        print("Unknown Type")
        return results
