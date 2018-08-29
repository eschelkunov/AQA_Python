from Phase1.Fibonacci import generate_fibonacci


class TestFibonacci:

    def test_fibonacci_function(self):
        actual_result = generate_fibonacci(10)
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        assert expected_result == actual_result, 'Fibonacci function returns results that are not matched'
