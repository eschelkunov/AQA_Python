Run locally:

1. In order to run API tests please use next command:
    
    'pytest -l -v ./tests/'
    
2. In order to run UI tests please use below command:
    
    'pytest -v -l ./ui/tests_ui/'
    
3. In order to run tests with allure reports use next:

   a) 'pytest -l -v --alluredir=%allure_results% ./tests/', or
    
    'pytest -l -v --alluredir=%allure_results% ./ui/tests_ui/',
    
   where '--alluredir=%allure_results%' is directory for reports
   
   b) then use 'serve' command to see your report:
   
      'allure serve %allure_results%/ -h localhost' , or
   
      'allure serve %allure_results%/', 
   
   where -h localhost - for running server locally