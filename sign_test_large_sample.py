import scipy.stats as st
import math
import scipy.stats


def sign_test_large_sample(df, column, md, alpha, alternate):
    """
                Infer types of values, possibly casting

                Parameters
                ----------
                df : data frame
                column : required column data of the df
                m :  Median of Population
                md : Expected value
                sample_size : Number of records in the column
                alpha : significance level
                alternate : Alternative Hypothesis (Three alternatives: not equal, greater than, less than)
    """

    minus_sign = df[df[column.name] < md][column.name]
    plus_sign = df[df[column.name] > md][column.name]
    equals = df[df[column.name] == md][column.name]
    len_minus_sign = len(minus_sign)
    len_plus_sign = len(plus_sign)
    len_equals = len(equals)
    sample_size = len(column)

    table_result = {'Negative Differences': len_minus_sign, 'Positive Differences': len_plus_sign, 'Ties': len_equals,
                    'Total': sample_size}
    print('\n', table_result)

    results = {'Variable': "", 'Test Statistic': "", 'Critical Value': "", "P-value": ""}

    if sample_size >= 30:

        if alternate == 'not equal':

            print('\n Hypothesis')
            print('\n Null Hypothesis: m is equal to', md)
            print('\n Alternative Hypothesis: m is not equal to', md)

            s = min(len_minus_sign, len_plus_sign)

            """Calculation test statistic with continuity correction"""

            test_statistic = ((s - 0.5) - sample_size * 0.5) / math.sqrt(
                sample_size * 0.5 * 0.5)

            a = 1 - ((alpha / 2) / 100)
            z_critical = round(st.norm.ppf(a), 2)
            p_value = scipy.stats.norm.sf(abs(test_statistic)) * 2
            p_value = round(p_value, 4)

            print('\n Rejection Criteria: Reject Null Hypothesis at', alpha,
                  '% level of significance if the test statistic '
                  '(Z)< -', z_critical, 'or test statistic (Z)>', z_critical)

            print('\n Test Results')
            results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                       'Lower Critical Value': -z_critical, 'Upper Critical Value': z_critical, 'P-value': p_value}
            print('\n', results)

            return results

        elif alternate == 'greater than':

            print('\n Hypothesis')
            print('\n Null Hypothesis: m is equal to', md)
            print('\n Alternative Hypothesis: m is greater than', md)

            s = len_minus_sign

            """Calculation test statistic with continuity correction"""

            test_statistic = ((s - 0.5) - sample_size * 0.5) / math.sqrt(
                sample_size * 0.5 * 0.5)

            a = 1 - (alpha / 100)
            z_critical = round(st.norm.ppf(a), 2)
            p_value = scipy.stats.norm.sf(abs(test_statistic))
            p_value = round(p_value, 4)

            print('\n Rejection Criteria: Reject Null Hypothesis at', alpha, '% level of significance '
                                                                             'if the test statistic (Z)>', z_critical)
            print('\n Test Results')
            results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                       'Critical Value': z_critical,
                       'P-value': p_value}
            print('\n', results)

            return results

        elif alternate == 'less than':

            print('\n Hypothesis')
            print('\n Null Hypothesis: m is equal to', md)
            print('\n Alternative Hypothesis: m is less than', md)

            s = len_plus_sign

            """Calculation test statistic with continuity correction"""

            test_statistic = ((s - 0.5) - sample_size * 0.5) / math.sqrt(
                sample_size * 0.5 * 0.5)

            a = 1 - (alpha / 100)
            z_critical = round(st.norm.ppf(a), 2)
            p_value = scipy.stats.norm.sf(abs(test_statistic))
            p_value = round(p_value, 4)

            print('\n Rejection Criteria: Reject Null Hypothesis at', alpha,
                  '% level of significance if the test statistic (Z)<-', z_critical)

            print('\n Test Results')
            results = {'Variable': column.name, 'Test Statistic': round(test_statistic, 4),
                       'Critical Value': -z_critical, 'P-value': p_value}
            print('\n', results)

            return results

    else:
        print('\n Since sample size is less than 30, Sign Test for Small Sample is recommended to apply for the data.')

    return results


