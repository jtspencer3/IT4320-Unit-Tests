
import unittest
import datetime


class TestInput(unittest.TestCase):

    def test_symbol(getInput):
        symbol = "GOOGL"
        getInput.assertLess(len(symbol), 7, msg="Stock symbol is larger than seven characters")
        getInput.assertTrue(symbol.isupper(), msg="Stock symbol is lowercase")

    def test_chartType(getInput):
        chartType = 1
        getInput.assertLessEqual(chartType, 2, msg="Chart type is larger than 2")
        getInput.assertGreaterEqual(chartType, 1, msg="Chart type is less than 1")
        getInput.assertTrue(type(chartType) == int, msg="Chart type is not numeric")

    def test_timeSeries(getInput):
        timeSeries = 1
        getInput.assertLessEqual(timeSeries, 4, msg="Time series is larger than 4")
        getInput.assertGreaterEqual(timeSeries, 1, msg="Time series is less than 1")
        getInput.assertTrue(type(timeSeries) == int, msg="Time series is not numeric")

    def test_startDate(getInput):
        startDate = datetime.datetime.strptime("2000-01-23", "%Y-%m-%d").date()
        testDate = datetime.date
        getInput.assertIsInstance(startDate, testDate, msg="Start date is not a date object")

    def test_endDate(getInput):
        endDate = datetime.datetime.strptime("2000-01-23", "%Y-%m-%d").date()
        testDate = datetime.date
        getInput.assertIsInstance(endDate, testDate, msg="End date is not a date object")


if __name__ == '__main__':
    unittest.main()