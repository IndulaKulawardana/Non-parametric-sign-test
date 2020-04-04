from small_sample_sign_test_calculation import five_fifty_sample_cal, six_fifty_sample_cal, seven_fifty_sample_cal, \
    eight_fifty_sample_cal


def sign_test_small_sample(df, column, md, alpha, alternate):
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
    sample_size = len_minus_sign + len_plus_sign

    sample_info = {"column_data": column, "count_minus_sign": len_minus_sign, "count_plus_sign": len_plus_sign,
                   "count_equals": len_equals, "sample_size": sample_size}

    table_result = {'Negative Differences': len_minus_sign, 'Positive Differences': len_plus_sign,
                    'Ties': len_equals, 'Total': sample_size}

    print('\n', table_result)

    results = {'Variable': "", 'Test Statistic': "", 'Critical Value': ""}

    if 5 <= sample_size <= 50 and alpha == 5:

        results = five_fifty_sample_cal(sample_info, md, alpha, alternate, results)

        print('\n', results)
        return results

    elif 6 <= sample_size <= 50 and alpha == 2.5:

        results = six_fifty_sample_cal(sample_info, md, alpha, alternate, results)

        print('\n', results)
        return results

    elif 7 <= sample_size <= 50 and alpha == 1:

        results = seven_fifty_sample_cal(sample_info, md, alpha, alternate, results)

        print('\n', results)
        return results

    elif 8 <= sample_size <= 50 and alpha == 0.5:

        results = eight_fifty_sample_cal(sample_info, md, alpha, alternate, results)

        print('\n', results)
        return results

    elif sample_size < 5:

        print('\n', "Sample Size is too small to apply the Sign Test.")
        return results

    elif sample_size == 5 and alpha != 5:

        print('\n',
              "Select 5 % as a significance level since critical value is not available at the provided significance level.")
        return results

    elif sample_size == 6 and (alpha == 0.5 or alpha == 1):

        print('\n',
              "Do not select 1 % or 0.5 % as a significance level since critical value is not available at the provided significance level.")
        return results

    elif sample_size == 7 and alpha == 0.5:

        print('\n',
              "Do not select 0.5 % as a significance level since critical value is not available at the provided significance level.")

        return results

    else:
        print('\n', "Test can not be executed for values of the given parameters.")

    return results
