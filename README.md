# Dj_store_test_project

My Automation Test Project Python+Selenium

Website for the project: online store of musical instruments, professional studio and concert equipment https://www.dj-store.ru

Tests in the project:

1. Selecting a product in the catalog and placing an order 
    

    pytest -s -v tests/test_buy_product.py::test_select_product
   

    With a report Allure 
    pytest --alluredir=test_results/ tests/test_buy_product.py::test_select_product


2. Authorization
   

    pytest -s -v tests/test_authorization::test_login_logout

    With a report Allure
    pytest --alluredir=test_results/ tests/test_authorization::test_login_logout


3. Change of region


    pytest -s -v tests/test_region_change.py::test_region_change

    With a report Allure
    pytest --alluredir=test_results/ tests/test_region_change.py::test_region_change







