"# AQA_Python" 

1. To run API tests use: 'pytest -l -v ./tests'
2. To run UI tests use: 'pytest -l -v ./ui/tests_ui/'
3. To run tests with allure reports:
    a) 'pytest -l -v --alluredir=%allure_results% ./tests'          (generating report for API)
       'pytest -l -v --alluredir=%allure_results% ./ui/tests_ui/'   (generating report for UI)
       
    b) 'allure serve %allure_results%' , or
       'allure serve %allure_results% -h localhost' (for opening reports locally)