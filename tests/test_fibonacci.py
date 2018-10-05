import allure

from my_code.fibonacci import generate_fibonacci


@allure.story('Test fibonacci')
class TestFibonacci:

    @allure.step
    @allure.title('Test fibonacci function')
    def test_fibonacci_function(self):
        actual_result = generate_fibonacci(10)
        expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        assert expected_result == actual_result, 'Fibonacci function returns results that are not matched with expected'

    @allure.step
    @allure.title('Test fibonacci with negative value')
    def test_fib_with_negative_value(self):
        assert generate_fibonacci(-5) == False
